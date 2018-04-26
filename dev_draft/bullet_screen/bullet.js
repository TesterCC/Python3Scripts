
 function messaction(ppp) {
        ppp.addClass("changmessage");
    }

    function messstop(ppp) {
        ppp.hide();
    }

    function pushtext(){
        var message=$("#message").val();
		if(message.length>0){
			$("#fontdiv").append("<pre class='oldp' style='width: "+message.length+"em'>"+message+"</pre>");
			$("#message").val("");
			var ppp= $("pre").last();
			//移动弹幕
			setTimeout(function(){
				messaction(ppp);
			},100);
			//隐藏弹幕
			setTimeout(function(){
				messstop(ppp);
			},8500);
		}
    };

    document.onkeydown=function(event){
        var e = event || window.event || arguments.callee.caller.arguments[0];
        if(e&&e.keyCode==13){
            //要做的事情
			e.preventDefault();
			var messvalue=$("#message").val();
			if(messvalue.length>0){
				pushtext();
			}
        }
    };
