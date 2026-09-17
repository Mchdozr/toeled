(function () {
  "use strict";

  var REDUCE = window.matchMedia("(prefers-reduced-motion: reduce)");
  var LERP = 0.24;

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
    if (!video) return;

    video.muted = true;
    video.defaultMuted = true;
    video.playsInline = true;
    video.setAttribute("playsinline", "");
    video.setAttribute("webkit-playsinline", "");
    video.preload = "auto";
    video.controls = false;
    video.pause();

    if (REDUCE.matches) {
      root.classList.add("is-static");
      try {
        video.currentTime = 0;
      } catch (e) {}
      return;
    }

    var target = 0;
    var current = 0;

    function durationOf() {
      var d = video.duration;
      return d && isFinite(d) && d > 0.05 ? d : 0;
    }

    function unlock() {
      video.muted = true;
      var play = video.play();
      if (play && typeof play.then === "function") {
        play
          .then(function () {
            video.pause();
          })
          .catch(function () {});
      } else {
        video.pause();
      }
    }

    function applyTime() {
      var duration = durationOf();
      if (!duration || video.seeking) return;
      var next = current * Math.max(0, duration - 0.04);
      if (Math.abs(video.currentTime - next) < 0.02) return;
      try {
        video.currentTime = next;
      } catch (e) {}
    }

    function tick() {
      target = progressOf(root);
      current += (target - current) * LERP;
      if (Math.abs(target - current) < 0.0005) current = target;
      applyTime();
      requestAnimationFrame(tick);
    }

    loadSeekable(video, function () {
      unlock();
      window.addEventListener("touchstart", unlock, { passive: true, once: true });
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
