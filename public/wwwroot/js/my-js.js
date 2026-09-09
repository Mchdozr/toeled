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
function AjaxInitForm(formObj, btnObj, isDialog, urlObj, callback) {
    var argNum = arguments.length; //参数个数    
    $(formObj).Validform({
        tiptype: 3,
        callback: function (form) {
            //AJAX提交表单
            $(form).ajaxSubmit({
                beforeSubmit: formRequest,
                success: formResponse,
                error: formError,
                url: $(formObj).attr("url"),
                type: "post",
                dataType: "json",
                timeout: 60000
            });
            return false;
        }
    });

    //表单提交前
    function formRequest(formData, jqForm, options) {
        $(btnObj).prop("disabled", true);
        $(btnObj).val("提交中...");
    }

    //表单提交后
    function formResponse(data, textStatus) {
        $(btnObj).prop("disabled", false);
        if (argNum == 5) {
            callback();
        }
        if (data.status == 1) {
            $(btnObj).val("提交成功");
            //是否提示，默认不提示
            if (isDialog == 1) {
                swal({
                    title: data.msg,
                    icon: "success",
                }).then(function (value) {
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
        }
        else {
            swal({
                title: data.msg,
                icon: "warning"
            }).then(function (value) {
                if (data.url) {
                    location.href = data.url;
                }
            });
            $(btnObj).val("重新提交");
        }
    }
    //表单提交出错
    function formError(XMLHttpRequest, textStatus, errorThrown) {
        swal({
            title: 'Status：' + textStatus + '；Tips：' + errorThrown,
            icon: "error"
        });
        if (argNum == 5) {
            callback();
        }
        $(btnObj).prop("disabled", false);
        $(btnObj).val("重新提交");
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
            });

            mobileNav.querySelectorAll("a").forEach(function (link) {
                link.addEventListener("click", function () {
                    mobileNav.hidden = true;
                    mobileToggle.setAttribute("aria-expanded", "false");
                    document.body.classList.remove("tl-nav-open");
                });
            });
        }

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