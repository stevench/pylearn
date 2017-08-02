/**
 * Created by steven on 17-7-31.
 */
//用户登录
function userLogin(){
    var username = $("#username").val();
    var password = $("#password").val();
    if(username.length == 0 || password.length == 0){
        alert("用户名或密码不能为空!");
        return false;
    }
    $.ajax({
        url:"/login",
        method:'post',
        async:true,
        data:{'username':username,'password':password},
        timeout:5000,
        dataType:'json',
        success:function(data){
            var flag = data.flag;
            if(flag != 1){
                alert('用户登录失败！');
                return false;
            }
            //关闭模态框
            $("#myLogin").modal("hide");
            $("#menus").show();
            $("#menu_login").hide();
            return true;
        },
        error:function(){
            $("#myLogin").modal("hide");
            alert("服务器出错!");
            return false;
        },
        });
}

//用户注册
function userRegister(){
    var username = $("#registername").val();
    var password = $("#registerpassword").val();
    var passwordagine = $("#registerpasswordagine").val();
    var email = $("#email").val();
    if(username.length == 0 || password.length == 0 || passwordagine == 0){
        alert("用户名或密码不能为空!");
        return false;
    }
    if(password != passwordagine){
        alert("两次密码输入不一致!")
        return false;
    }
    $.ajax({
        url:"/register",
        method:'post',
        async:true,
        data:{'username':username,'password':password,"email":email},
        timeout:5000,
        dataType:'json',
        success:function(data){
            var flag = data.flag;
            if(flag != 1){
                $("#myRegister").modal("hide");
                alert('用户注册失败！');
                return false;
            }
            alert("用户注册成功！");
            $("#myRegister").modal("hide");
            $("#myLogin").modal("show");
            return true;
        },
        error:function(){
            $("#myRegister").modal("hide");
            alert("服务器出错!");
            return false;
        },
        });
}

function getLogger(){
    $.ajax({
        url:"/logger",
        method:'post',
        async:true,
        data:{'username':username},
        timeout:5000,
        dataType:'json',
        success:function(data){

            return true;
        },
        error:function(){
            alert("服务器出错!");
            return false;
        },
        });
}
