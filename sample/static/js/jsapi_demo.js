/* --- root fontSize begin --- */
(function (doc, win) {
    var _root = doc.documentElement,
            resizeEvent = 'orientationchange' in window ? 'orientationchange' : 'resize',
            resizeCallback = function () {
                var clientWidth = _root.clientWidth,
                        fontSize = 20;
                if (!clientWidth) return;
                if(clientWidth < 640) {
                    fontSize = 20 * (clientWidth / 320);
                } else if (clientWidth >= 640 && clientWidth < 768) {
                    fontSize = 20 * (640 / 320);
                } else {
                    fontSize = 20;
                }
                _root.style.fontSize = fontSize + 'px';
            };
    if (!doc.addEventListener) return;
    win.addEventListener(resizeEvent, resizeCallback, false);
    doc.addEventListener('DOMContentLoaded', resizeCallback, false);
})(document, window);
/* end root fontSize */

/* --- API获取签名信息 begin --- */
var _config = null; // 定义全局变量_config，初始值为null，用来接收API获取到的签名信息
var getConfig = $.ajax({
    type: 'GET',
    url: '/api/v1/jsapi',
    data: {
        url: window.location.href,
    },
    success: function(data){
        if(data.code == 0){
            _config = data.data;
        }else{
            dd.device.notification.alert({
                message: "Data error: failed to get signature.",
                title: "Huooo",
                buttonName: "OK"
            });
        }
    },
    error: function(data){
        dd.device.notification.alert({
            message: "API error: failed to API request.",
            title: "Huooo",
            buttonName: "OK"
        });
    },
    complete: function(data){
        // alert('3. 请求完成时：'+JSON.stringify(_config));
        DDConfig(_config);
    }
});
// alert('1. API请求开始：'+JSON.stringify(getConfig));
/* --- end API获取签名信息 --- */
/* --- DD Config Function --- */
function DDConfig(_config){
    // 弹出DD全局变量
    // alert('4. DD全局变量：'+JSON.stringify(dd));
    // 配置DD签名等相关信息
    dd.config({
        agentId : _config.agentId,
        corpId : _config.corpId,
        timeStamp : _config.timeStamp,
        nonceStr : _config.nonceStr,
        signature : _config.signature,
        jsApiList : [
            'runtime.info',
            'biz.contact.choose',
            'device.notification.confirm',
            'device.notification.alert',
            'device.notification.prompt',
            'device.notification.toast',
            'biz.ding.post',
            'biz.util.openLink',
            'device.geolocation.get',
            'biz.util.scan',
            'biz.user.get',
            'biz.navigation.close',
            'biz.util.open',
            'biz.chat.chooseConversationByCorpId'
        ]
    });
    dd.ready(function(){
        dd.biz.user.get({
            onSuccess: function (info) {
                // alert('6. userGet success: ' + JSON.stringify(info));
                // alert('7. user nickname: ' + JSON.stringify(info.nickName));
                $('#nickname').val(info.nickName);
            },
            onFail: function (err) {
                dd.device.notification.alert({
                    message: "DD userGet fail: " + JSON.stringify(err),
                    title: "Huooo",
                    buttonName: "OK"
                });
            }
        });
    });
    dd.error(function(err) {
        dd.device.notification.alert({
            message: "DD error: " + JSON.stringify(err),
            title: "Huooo",
            buttonName: "OK"
        });
    });
}
/* --- end DD API --- */

// 业务逻辑
$("#login").click(function(){
    dd.runtime.permission.requestAuthCode({
        corpId: "corpid",
        onSuccess: function(result) {
            window.location.href = "/login_callback?code=" + result["code"]
        /*{
            code: 'hYLK98jkf0m' //string authCode
        }*/
        },
        onFail : function(err) {
            alert("失败:" + JSON.stringify(err))
        }
    })
});

$("#scan").click(function(){
    dd.biz.util.scan({
        type: "all" , // type 为 all、qrCode、barCode，默认是all。
        onSuccess: function(data) {
            alert("成功:" + JSON.stringify(data))
        },
       onFail : function(err) {
            alert("失败:" + JSON.stringify(err))
       }
    })
});


$("#image").click(function(){
    dd.biz.util.previewImage({
        urls: [
            "https://www.baidu.com/img/bd_logo1.png",
            "https://box.bdimg.com/static/fisp_static/common/img/searchbox/logo_news_276_88_1f9876a.png",
            "https://tb2.bdstatic.com/tb/static-common/img/search_logo_big_v1_8d039f9.png"
        ],//图片地址列表
        current: "https://www.baidu.com/img/bd_logo1.png",//当前显示的图片链接
        onSuccess : function(data) {
            alert("成功:" + JSON.stringify(data))
        },
        onFail : function(err) {
            alert("失败:" + JSON.stringify(err))
        }
    })
});

$("#alert").click(function(){
    dd.device.notification.alert({
        message: "亲爱的",
        title: "提示",//可传空
        buttonName: "收到",
        onSuccess : function(data) {
            alert("成功:" + JSON.stringify(data))
        },
        onFail : function(err) {
            alert("失败:" + JSON.stringify(err))
        }
    });
});

$("#map").click(function(){
    dd.device.geolocation.get({
        targetAccuracy : Number,
        coordinate : Number,
        withReGeocode : Boolean,
        useCache:true, //默认是true，如果需要频繁获取地理位置，请设置false
        onSuccess : function(data) {
            alert("成功:" + JSON.stringify(data))
            /* 高德坐标 result 结构
            {
                longitude : Number,
                latitude : Number,
                accuracy : Number,
                address : String,
                province : String,
                city : String,
                district : String,
                road : String,
                netType : String,
                operatorType : String,
                errorMessage : String,
                errorCode : Number,
                isWifiEnabled : Boolean,
                isGpsEnabled : Boolean,
                isFromMock : Boolean,
                provider : wifi|lbs|gps,
                isMobileEnabled : Boolean
            }
            */
        },
        onFail : function(err) {
            alert("失败:" + JSON.stringify(err))
        }
    });
});


$("#device").click(function(){
    dd.device.base.getPhoneInfo({
        onSuccess : function(data) {
            alert("成功:" + JSON.stringify(data))
            /*
            {
                screenWidth: 1080, // 手机屏幕宽度
                screenHeight: 1920, // 手机屏幕高度
                brand:'Mi'， // 手机品牌
                model:'Note4', // 手机型号
                version:'7.0'. // 版本
                netInfo:'wifi' , // 网络类型 wifi／4g／3g
                operatorType :'xx' // 运营商信息
            }
            */
        },
        onFail : function(err) {
            alert("失败:" + JSON.stringify(err))
        }
    });
});
