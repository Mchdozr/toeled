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