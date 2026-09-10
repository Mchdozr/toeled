function CaseSiteSearch(send_url, Tgs1, Tgs2, Tgs3, Tgs4) {
    var queryConfig = {
        "scenarios": $.trim($(Tgs1).val()),
        "area": $.trim($(Tgs2).val()),
        "spacing": $.trim($(Tgs3).val()),
        "location": $.trim($(Tgs4).val())
    };
    var setQueryConfig = function () {
        var _str = "";
        for (var o in queryConfig) {
            if (queryConfig[o] != '') {
                _str += o + "=" + encodeURI(queryConfig[o]) + "&";
            }
        }
        var _str = _str.substring(0, _str.length - 1);
        return _str;
    }
    var params = setQueryConfig();
    if (params.length > 0) {
        window.location.href = send_url + "?" + params;
    }
    else {
        window.location.href = send_url;
    }
    return false;
}
function ProductSiteSearch(send_url, Tgs1, Tgs2, Tgs3) {
    var queryConfig = {
        "models": $.trim($(Tgs1).val()),
        "scenarios": $.trim($(Tgs2).val()),
        "spacing": $.trim($(Tgs3).val())
    };
    var setQueryConfig = function () {
        var _str = "";
        for (var o in queryConfig) {
            if (queryConfig[o] != '') {
                _str += o + "=" + encodeURI(queryConfig[o]) + "&";
            }
        }
        var _str = _str.substring(0, _str.length - 1);
        return _str;
    }
    var params = setQueryConfig();
    if (params.length > 0) {
        window.location.href = send_url + "?" + params;
    }
    else {
        window.location.href = send_url;
    }
    return false;
}
function SiteSearch(send_url, divTgs) {
    var queryConfig = {
        "se": $.trim($(divTgs).val())
    };
    var setQueryConfig = function () {
        var _str = "";
        for (var o in queryConfig) {
            if (queryConfig[o] != '') {
                _str += o + "=" + encodeURI(queryConfig[o]) + "&";
            }
        }
        var _str = _str.substring(0, _str.length - 1);
        return _str;
    }
    var params = setQueryConfig();

    if (params.length > 0) {
        window.location.href = send_url + "?" + params;
    }
    return false;
}

//切换验证码
function toggleCode() {
    $(".verycode").attr("src", "/Manage_SW/ValidateCode?s=" + Math.random());
}
var showmsg = function (msg) {
    if (msg != '' && $.trim(msg)) {
        swal({
            title: msg,
            icon: "warning"
        });
    }
}

var TOELED_FORM_ENDPOINT = "https://formsubmit.co/ajax/info@ledajans.com";

function resolveFormSubmitUrl(formObj) {
    var url = $.trim($(formObj).attr("url") || $(formObj).attr("action") || "");
    if (!url || url === "#" || url.indexOf("#") === 0) {
        return TOELED_FORM_ENDPOINT;
    }
    return url;
}

function normalizeFormSubmitResponse(data) {
    if (data && typeof data.status !== "undefined") {
        return data;
    }
    if (data && data.success) {
        return {
            status: 1,
            msg: "Mesajınız alındı. En kısa sürede dönüş yapacağız."
        };
    }
    if (data && data.message) {
        return {
            status: 1,
            msg: data.message
        };
    }
    return {
        status: 0,
        msg: "Mesaj gönderilemedi. Lütfen tekrar deneyin."
    };
}

function setSubmitButtonLabel(btnObj, text) {
    var $btn = $(btnObj);
    if ($btn.is("input")) {
        $btn.val(text);
    } else {
        $btn.text(text);
    }
}

function getSubmitButtonLabel(btnObj) {
    var $btn = $(btnObj);
    if ($btn.is("input")) {
        return $btn.val();
    }
    return $btn.text();
}

function AjaxInitForm(formObj, btnObj, isDialog, urlObj, callback) {
    var argNum = arguments.length;
    var defaultBtnLabel = getSubmitButtonLabel(btnObj);

    $(formObj).Validform({
        tiptype: 3,
        callback: function (form) {
            var submitUrl = resolveFormSubmitUrl(formObj);
            var payload = $(form).serializeArray();

            if (submitUrl.indexOf("formsubmit.co") !== -1) {
                payload.push({ name: "_subject", value: "Toeled - İletişim Formu" });
                payload.push({ name: "_captcha", value: "false" });
                payload.push({ name: "_template", value: "table" });
                payload.push({ name: "_form", value: $(formObj).attr("id") || "contact" });
            }

            setSubmitButtonLabel(btnObj, "Gönderiliyor...");
            $(btnObj).prop("disabled", true);

            $.ajax({
                url: submitUrl,
                type: "POST",
                data: $.param(payload),
                dataType: "json",
                timeout: 60000,
                success: function (data, textStatus) {
                    formResponse(normalizeFormSubmitResponse(data), textStatus);
                },
                error: formError
            });
            return false;
        }
    });

    function formResponse(data, textStatus) {
        $(btnObj).prop("disabled", false);
        if (argNum == 5) {
            callback();
        }
        if (data.status == 1) {
            setSubmitButtonLabel(btnObj, "Gönderildi");
            if (isDialog == 1) {
                swal({
                    title: data.msg,
                    icon: "success",
                }).then(function () {
                    if (data.url) {
                        location.href = data.url;
                    } else if ($(urlObj) && $(urlObj).length > 0) {
                        location.href = $(urlObj).val();
                    } else {
                        location.reload();
                    }
                });
            } else {
                if (data.url) {
                    location.href = data.url;
                } else if ($(urlObj) && $(urlObj).length > 0) {
                    location.href = $(urlObj).val();
                } else {
                    location.reload();
                }
            }
        } else {
            swal({
                title: data.msg,
                icon: "warning"
            }).then(function () {
                if (data.url) {
                    location.href = data.url;
                }
            });
            setSubmitButtonLabel(btnObj, defaultBtnLabel);
        }
    }

    function formError(XMLHttpRequest, textStatus, errorThrown) {
        swal({
            title: "Mesaj gönderilemedi. Lütfen daha sonra tekrar deneyin veya info@ledajans.com adresine yazın.",
            icon: "error"
        });
        if (argNum == 5) {
            callback();
        }
        $(btnObj).prop("disabled", false);
        setSubmitButtonLabel(btnObj, defaultBtnLabel);
    }
}

(function initToeledMotion() {
    if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        return;
    }

    document.documentElement.classList.add("sd-motion");

    if (!document.querySelector('meta[name="view-transition"]')) {
        var meta = document.createElement("meta");
        meta.setAttribute("name", "view-transition");
        meta.setAttribute("content", "same-origin");
        document.head.appendChild(meta);
    }

    function activateReveals() {
        var nodes = document.querySelectorAll("[hsm]");
        if (!nodes.length || !("IntersectionObserver" in window)) {
            for (var i = 0; i < nodes.length; i++) {
                nodes[i].classList.add("in");
            }
            return;
        }

        var groups = document.querySelectorAll(".hsms");
        for (var g = 0; g < groups.length; g++) {
            var kids = groups[g].querySelectorAll("[hsm]");
            for (var k = 0; k < kids.length && k < 8; k++) {
                kids[k].style.transitionDelay = (k * 0.08) + "s";
            }
        }

        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) {
                    return;
                }
                entry.target.classList.add("in");
                io.unobserve(entry.target);
            });
        }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });

        for (var n = 0; n < nodes.length; n++) {
            io.observe(nodes[n]);
        }
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", activateReveals);
    } else {
        activateReveals();
    }
})();

(function initToeledNavigation() {
    function boot() {
        var header = document.querySelector("[data-tl-header]");
        if (!header) {
            return;
        }

        var triggers = Array.prototype.slice.call(header.querySelectorAll("[data-tl-menu]"));
        var panels = Array.prototype.slice.call(header.querySelectorAll("[data-tl-panel]"));
        var mobileToggle = header.querySelector("[data-tl-mobile-toggle]");
        var mobileNav = header.querySelector("[data-tl-mobile-nav]");
        var lastTrigger = null;
        var closeTimer = null;

        function closeDesktopMenus(restoreFocus) {
            triggers.forEach(function (trigger) {
                trigger.setAttribute("aria-expanded", "false");
            });
            panels.forEach(function (panel) {
                panel.setAttribute("aria-hidden", "true");
                panel.removeAttribute("data-open");
            });
            if (restoreFocus && lastTrigger) {
                lastTrigger.focus();
            }
        }

        function openMenu(trigger) {
            var panel = document.getElementById(trigger.getAttribute("aria-controls"));
            closeDesktopMenus(false);
            if (!panel) {
                return;
            }
            lastTrigger = trigger;
            trigger.setAttribute("aria-expanded", "true");
            panel.setAttribute("aria-hidden", "false");
            panel.setAttribute("data-open", "true");
        }

        triggers.forEach(function (trigger) {
            var group = trigger.closest("[data-tl-group]");
            trigger.addEventListener("click", function () {
                if (trigger.getAttribute("aria-expanded") === "true") {
                    closeDesktopMenus(false);
                } else {
                    openMenu(trigger);
                }
            });
            group.addEventListener("mouseenter", function () {
                window.clearTimeout(closeTimer);
                openMenu(trigger);
            });
            group.addEventListener("mouseleave", function () {
                closeTimer = window.setTimeout(function () {
                    closeDesktopMenus(false);
                }, 130);
            });
            group.addEventListener("focusout", function (event) {
                if (!group.contains(event.relatedTarget)) {
                    closeDesktopMenus(false);
                }
            });
        });

        document.addEventListener("click", function (event) {
            if (!header.contains(event.target)) {
                closeDesktopMenus(false);
            }
        });

        document.addEventListener("keydown", function (event) {
            if (event.key === "Escape") {
                closeDesktopMenus(true);
                if (mobileNav && !mobileNav.hidden) {
                    mobileNav.hidden = true;
                    mobileToggle.setAttribute("aria-expanded", "false");
                    mobileToggle.setAttribute("aria-label", "Menüyü aç");
                    document.body.classList.remove("tl-nav-open");
                    header.classList.remove("tl-nav-open");
                    mobileToggle.focus();
                }
            }
        });

        if (mobileToggle && mobileNav) {
            mobileToggle.addEventListener("click", function () {
                var opening = mobileNav.hidden;
                mobileNav.hidden = !opening;
                mobileToggle.setAttribute("aria-expanded", String(opening));
                mobileToggle.setAttribute("aria-label", opening ? "Menüyü kapat" : "Menüyü aç");
                document.body.classList.toggle("tl-nav-open", opening);
                header.classList.toggle("tl-nav-open", opening);
            });

            mobileNav.querySelectorAll("a").forEach(function (link) {
                link.addEventListener("click", function () {
                    mobileNav.hidden = true;
                    mobileToggle.setAttribute("aria-expanded", "false");
                    document.body.classList.remove("tl-nav-open");
                    header.classList.remove("tl-nav-open");
                });
            });
        }

        var hasHeroUnderHeader = !!document.querySelector("main > .home-swiper, main > .public-banner, main > .swiper.home-swiper");
        if (hasHeroUnderHeader) {
            header.classList.add("tl-header-over-media");
        }

        function updateHeaderOnScroll() {
            var atTop = window.scrollY <= 12;
            header.classList.toggle("is-at-top", atTop);
        }

        updateHeaderOnScroll();
        window.addEventListener("scroll", updateHeaderOnScroll, { passive: true });

        window.addEventListener("resize", function () {
            if (window.innerWidth > 1024 && mobileNav && !mobileNav.hidden) {
                mobileNav.hidden = true;
                mobileToggle.setAttribute("aria-expanded", "false");
                document.body.classList.remove("tl-nav-open");
            }
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", boot);
    } else {
        boot();
    }
})();

//只允许输入数字
function checkNumber(e) {
    var keynum = window.event ? e.keyCode : e.which;
    if ((48 <= keynum && keynum <= 57) || (96 <= keynum && keynum <= 105) || keynum == 8) {
        return true;
    } else {
        return false;
    }
}
//只允许输入小数
function checkForFloat(obj, e) {
    var isOK = false;
    var key = window.event ? e.keyCode : e.which;
    if ((key > 95 && key < 106) || //小键盘上的0到9  
        (key > 47 && key < 60) ||  //大键盘上的0到9  
        (key == 110 && obj.value.indexOf(".") < 0) || //小键盘上的.而且以前没有输入.  
        (key == 190 && obj.value.indexOf(".") < 0) || //大键盘上的.而且以前没有输入.  
        key == 8 || key == 9 || key == 46 || key == 37 || key == 39) {
        isOK = true;
    } else {
        if (window.event) { //IE
            e.returnValue = false;   //event.returnValue=false 效果相同.    
        } else { //Firefox 
            e.preventDefault();
        }
    }
    return isOK;
}