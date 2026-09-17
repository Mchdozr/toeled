(function () {
  "use strict";

  var REDUCE = window.matchMedia("(prefers-reduced-motion: reduce)");
  var LERP = 0.22;
  var FRAME = 1 / 24;

  function clamp(n, a, b) {
    return Math.max(a, Math.min(b, n));
  }

  function progressOf(root) {
    var rect = root.getBoundingClientRect();
    var total = root.offsetHeight - window.innerHeight;
    if (total <= 1) return 0;
    return clamp(-rect.top / total, 0, 1);
  }

  function loadSeekable(video, done) {
    var src = video.getAttribute("src");
    if (!src || !window.fetch) {
      done();
      return;
    }
    fetch(src)
      .then(function (res) {
        return res.blob();
      })
      .then(function (blob) {
        var url = URL.createObjectURL(blob);
        video.src = url;
        video.addEventListener("loadedmetadata", done, { once: true });
        video.load();
      })
      .catch(function () {
        done();
      });
  }

  function initExplode(root) {
    var video = root.querySelector(".tl-pdp-explode-video");
    var pin = root.querySelector(".tl-pdp-explode-pin");
    if (!video) return;

    video.muted = true;
    video.defaultMuted = true;
    video.playsInline = true;
    video.setAttribute("playsinline", "");
    video.setAttribute("webkit-playsinline", "");
    video.preload = "auto";
    video.controls = false;
    video.style.pointerEvents = "none";
    if (pin) pin.style.willChange = "transform";

    if (REDUCE.matches) {
      root.classList.add("is-static");
      try {
        video.currentTime = 0;
      } catch (e) {}
      return;
    }

    var targetTime = 0;
    var smoothTime = 0;
    var pendingSeek = false;

    function durationOf() {
      var d = video.duration;
      return d && isFinite(d) && d > 0.05 ? d : 0;
    }

    function setTarget() {
      var duration = durationOf();
      if (!duration) return;
      targetTime = progressOf(root) * Math.max(0, duration - FRAME);
    }

    video.addEventListener("seeked", function () {
      pendingSeek = false;
    });

    function applyTime() {
      if (pendingSeek || video.seeking) return;
      if (video.readyState < 2) return;
      var duration = durationOf();
      if (!duration) return;
      var next = clamp(smoothTime, 0, duration);
      if (Math.abs(video.currentTime - next) < FRAME) return;
      pendingSeek = true;
      try {
        video.currentTime = next;
      } catch (e) {
        pendingSeek = false;
      }
    }

    function tick() {
      setTarget();
      smoothTime += (targetTime - smoothTime) * LERP;
      if (Math.abs(targetTime - smoothTime) < 0.0004) smoothTime = targetTime;
      applyTime();
      requestAnimationFrame(tick);
    }

    loadSeekable(video, function () {
      setTarget();
      smoothTime = targetTime;
      window.addEventListener("scroll", setTarget, { passive: true });
      requestAnimationFrame(tick);
    });
  }

  function boot() {
    var nodes = document.querySelectorAll("[data-tl-explode]");
    for (var i = 0; i < nodes.length; i += 1) initExplode(nodes[i]);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
