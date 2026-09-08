(function () {
  var share_url = encodeURI(location.href)
  var site_url = encodeURIComponent(location.origin)
  var share_title = encodeURIComponent(document.title)
  var share_pic = $("img:first").prop("src") || "" // 默认的分享图片
  var share_from = $("meta[name='site']").attr('content') || encodeURIComponent(document.title);
  var share_description = $("meta[name='description']").attr('content') || '';

  //QQ
  $("a[data-social='QQ']").click(function (e) {
    window.open('http://connect.qq.com/widget/shareqq/index.html?url=' + share_url + '&title=' + share_title + '&source=' + share_from + '&desc=' + share_description + '&pics=' + share_pic + '', 'newwindow')
  })

  //Sina Weibo新浪微博
  $("a[data-social='xinlang']").click(function (e) {
    var param = {
      url: share_url,
      appkey: '678438995',
      title: share_title,
      pic: share_pic,
      // ralateUid: '3061825921',
      rnd: new Date().valueOf()
    }
    var temp = []
    for (var p in param) {
      temp.push(p + '=' + encodeURIComponent(param[p] || ''))
    }
    window.open('http://service.weibo.com/share/share.php?' + temp.join('&'))
  })

  //QQ空间
  $("a[data-social='QQkongjian']").click(function (e) {
    window.open('http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=' + share_url + '&title=' + share_title + '&pics=' + share_pic + '&site=' + share_from + '', 'newwindow')
  })

  //facebook
  $("a[data-social='facebook']").click(function (e) {
    window.open('https://www.facebook.com/sharer/sharer.php?u=' + share_url + '&title=' + share_title + '&description=' + share_description + '&link=' + share_url + '&picture=' + share_pic + '', 'newwindow')
  })

  //twitter
  $("a[data-social='twitter']").click(function (e) {
    window.open('https://twitter.com/intent/tweet?text=' + share_title + '&url=' + share_url + '&via=' + site_url + '', 'newwindow')
  })

  //linkedin
  $("a[data-social='linkedin']").click(function (e) {
    window.open('http://www.linkedin.com/shareArticle?mini=true&ro=true&title=' + share_title + '&url=' + share_url + '&summary=' + share_description + '&source=' + share_from + '&armin=armin', 'newwindow')
  })

  //google
  $("a[data-social='google']").click(function (e) {
    window.open('https://plus.google.com/share?url=' + share_url + '', 'newwindow')
  })

  //douban
  $("a[data-social='douban']").click(function (e) {
    window.open('http://shuo.douban.com/!service/share?href=' + share_url + '&name=' + share_title + '&text=' + share_description + '&image=' + share_pic + '&starid=0&aid=0&style=11', 'newwindow')
  })

  //朋友网
  $("a[data-social='pengyouweb']").click(function (e) {
    window.open('http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?to=pengyou&url=' + share_url + '&pics=' + share_pic + '&title=' + share_title + '&site=' + share_from + '', 'newwindow')
  })

  //kaixin开心网
  $("a[data-social='kaixin']").click(function (e) {
    window.open('http://www.kaixin001.com/repaste/bshare.php?rtitle=' + share_title + '&rurl=' + share_url + '&from=' + share_from + '', 'newwindow')
  })

  //renren人人网
  $("a[data-social='renren']").click(function (e) {
    window.open('http://widget.renren.com/dialog/share?resourceUrl=' + share_url + '&title=' + share_title + '&images=' + share_pic + '', 'newwindow')
  })

  //tq腾讯微博
  $("a[data-social='tengxun']").click(function (e) {
    window.open('http://share.v.t.qq.com/index.php?c=share&a=index&title=' + share_title + '&site=' + share_from + '&pic=' + share_pic + '&url=' + share_url + '', 'newwindow')
  })

  $("a[data-social='weixin']").click(function (e) {
    $('body').append($('<div class="qrcode_mask"></div><div id="qrcode" class="qrcode none"></div>'))
    if (!$('#qrcode img').length) {
      var qrcode = new QRCode(document.getElementById('qrcode'), {
        text: share_url,
        width: 180,
        height: 180,
        colorDark: '#333333',
        colorLight: '#ffffff',
        correctLevel: QRCode.CorrectLevel.H
      })
    }

    !!$('.qrcode_msg').length || $('#qrcode').append('<p class="t_c qrcode_msg">点击右上角【...】开始分享</p><a class="weixin_close" href="javascript:;">暂不分享</a>')
    $('.qrcode_mask').fadeIn(0)
    $('#qrcode').fadeIn(100)
  })

  $('body').delegate('.weixin_close', 'click', function () {

    $('#qrcode, .qrcode_mask').remove()
  })
})();
