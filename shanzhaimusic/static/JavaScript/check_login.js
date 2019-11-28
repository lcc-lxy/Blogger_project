$.ajax({
    url:'http://127.0.0.1:8000/index/index_server',
    type:'get',
    dataType:'json',
    success:function(data){
        if (data.username){
            $('#login_box').html('<span class="dl">欢迎您 , '+data.username +' <a href="/personal">个人中心</a>   <a href="/index/exit/">注销</a></span>')
        }else{
            $('#login_box').html('<span class="dl"><a href="/user/login">登录/注册</a></span>')
        }
    }
})