<template>
    <div id='main' class="clearfix">
       <div id="logo" style="position:absolute;top:40px;left:0;">
            <img src="../../static/img/logo1.jpg" alt="">
        </div>
        <div id="content" class="clearfix" style="position:relative">
            <div class="c_left text-center">
                <div class="l_head">
                    <p class="mb-0">欢迎,</p>
                    <p>来到青年小栈</p>
                </div>
                <p class="l_middle mt-4">这是一个辅助年轻人自我管理的网站,如果你想知道这个网站有什么功能，你可以试着点击以下按钮</p>
                <button class="btn btn-lg border-info l_foot" @click="to_article()">功能介绍文档 <span class="glyphicon glyphicon-arrow-right"></span></button>
                <!-- <button class="btn btn-lg border-info l_foot" @click="to_forum">随便逛逛 <span class="glyphicon glyphicon-arrow-right"></span></button> -->
                <p class="l_tip text-warning mt-4">提示:网站中几乎所有的功能都是只提供给用户</p>
                
            </div>
            <div class="c_right">
                <div v-show="show" class="form" :class="translate">
                    <button class="btn float-right" @click="login_register_convert">注册<span class="glyphicon glyphicon-hand-right"></span></button>
                    <p class="text-center mb-0">登录</p>
                    <hr class="mt-2">
                    <div class="form-group mb-3">
                        <span class="glyphicon glyphicon-user"></span>
                        <label for="username">用户名</label>
                        <input type="text" class="form-control" id="username" name="username" :placeholder="username_lp">
                    </div>
                    <div class="form-group mb-3">
                        <span class="glyphicon glyphicon-lock"></span>
                        <label for="password">密码</label>
                        <input type="password" class="form-control" id="password" name="password" :placeholder="password_lp">
                    </div>
                    <div class="form-group">
                        <label class="avoid_login">
                            <input type="checkbox" id="avoid_login" style="display:none" v-model="avoid_login">
                            <div class="float-left" style="height:16px;width:16px;line-height:14px;border:1px solid #444;margin:4px 2px;border-radius:4px;text-align:center">
                                <span class="glyphicon glyphicon-ok" v-show="avoid_login" style="font-size:14px;color:#333;"></span>
                            </div>
                            <span style="font-size:15px;color:#555;cursor:pointer">记住我</span>
                        </label>
                    </div>
                    <div>
                        <button id="register" class="btn btn-block submit" @click="index_login">登录</button>
                    </div>
                </div>
                <div v-show="!show" class="form" :class="translate">
                    <button class="btn float-left" @click="login_register_convert"><span class="glyphicon glyphicon-hand-left">登录</span></button>
                    <p class="text-center mb-0">注册</p>
                    <hr class="my-1">
                    <div class="form-group mb-2">
                        <span class="glyphicon glyphicon-user"></span>
                        <label for="reg_username">用户名</label>
                        <input type="text" class="form-control" id="reg_username" name="reg_username" :placeholder="password_rp">
                    </div>
                    <div class="form-group mb-2">
                        <span class="glyphicon glyphicon-lock"></span>
                        <label for="reg_password">密码</label>
                        <input type="password" class="form-control" id="reg_password" name="reg_password" :placeholder="password_rp">
                    </div>
                    <div class="form-group mb-2">
                        <span class="glyphicon glyphicon-envelope"></span>
                        <label for="email">邮箱</label>
                        <input type="email" class="form-control" id="email" name="email" :placeholder="email_rp">
                    </div>
                    <div class="form-group mb-2">
                        <span class="glyphicon glyphicon-phone"></span>
                        <label for="phone">手机</label>
                        <input type="text" class="form-control" id="phone" name="phone" :placeholder="phone_rp">
                    </div>
                    <div>
                        <button id="login" class="btn btn-block submit" @click="index_register">注册</button>
                    </div>
                </div>
            </div>
            <div class="beian p-2 text-center" style="position:absolute; bottom:0;width:100%">
                <a href="http://www.beian.miit.gov.cn" target="_blank" class="text-dark text-decoration-none" style="font-size:14px;color:#666;">鄂ICP备200002048</a>
            </div>
        </div>
    </div>
</template>
<script>
import {avoidLogin, login, register} from '../assets/js/apis/index.js'
import '../assets/css/myheader.css'
import '../assets/css/myfooter.css'
import '../assets/css/index.css'

export default {
    name: 'Index',
    data () {
        return {
            show: true,
            translate: {
                translate: this.show==false,
            },
            avoid_login: false,
            username_lp: "6~16位英文,数字,下划线组成",
            password_lp: "6~16位英文,数字,下划线组成",
            username_rp: "6~16位英文,数字,下划线组成",
            password_rp: "6~16位英文,数字,下划线组成",
            phone_rp: "请输入手机号码",
            email_rp: "请输入邮箱"
        }
    },
    methods: {
        login_register_convert(){
            this.translate.translate = true;
            setTimeout(()=>{
                this.show = !this.show;
                this.translate.translate = false;
            },1000)
            
        },
        login_validate(){
            var username  = document.getElementById("username");
            var password = document.getElementById("password");
            var re = /^[0-9 a-z A-Z _]{6,16}$/;
            if (!re.test(username.value)){
                alert('请输入有效格式的用户名');
                username.value = "";
                username.focus();
                return false
            }
            if (!re.test(password.value)){
                alert('请输入有效格式的密码');
                password.value = "";
                password.focus();
                return false
            }
            return {username:username.value, password:password.value}
        },
        reg_validate(){
            var username = document.getElementById("reg_username");
            var password = document.getElementById("reg_password");
            var email = document.getElementById("email");
            var phone = document.getElementById("phone");
            var re_1 = /^[0-9 a-z A-Z _]{6,16}$/;
            var re_phone = /^1[3-9]\d{9}$/;
            var re_email = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
            if (!re_1.test(username.value)){
                alert('请输入有效格式的用户名');
                username.value = "";
                username.focus();
                return false
            }
            if (!re_1.test(password.value)){
                alert('请输入有效格式的密码');
                password.value = "";
                password.focus();
                return false
            }
            if (!re_email.test(email.value)){
                alert('请输入有效格式的邮箱');
                email.value = "";
                email.focus();
                return false
            }
            if (!re_phone.test(phone.value)){
                alert('请输入有效格式的手机号码');
                phone.value = "";
                phone.focus();
                return false;
            }
            return {username:username.value,password:password.value,email:email.value,phone:phone.value}
        },
        index_login(){
            if (this.login_validate()){
                var avoid_login = this.avoid_login;
                var data = this.login_validate();
                data.avoid_login = avoid_login;
                login(data).then(result=>{
                    if (result.code==200){
                        localStorage.setItem('ytoken', result.token);
                        localStorage.setItem('user_id', result.id);
                        this.$router.push("/todo");
                    }else{
                        alert(result.error);
                    }
                })
            }
            
        },
        index_register(){
            if (this.reg_validate()){
                var data = this.reg_validate();
                register(data).then(result=>{
                    if (result.code==200){
                        localStorage.setItem('ytoken', result.token);
                        localStorage.setItem('user_id', result.id)
                        this.$router.push("/todo");
                    }else{
                        alert(result.error)
                    }
                })
            }
        },
        to_article(){
            var {href} = this.$router.resolve({path: '/article', query:{author_id:1, article_id:999}});
            window.open(href, '_blank');
        }
    },
    created(){
        var ytoken = window.localStorage.getItem('ytoken');
        if (ytoken) {
            avoidLogin(ytoken).then(
                result=>{
                    if (result.code==200){
                        this.$router.push("/todo");
                    }else if(result.code==10202){
                        alert('会话已过期,请重新登陆');
                        localStorage.removeItem('ytoken');
                        localStorage.removeItem('user_id');
                        this.$router.push({name:'Index'});
                    }
                }
            )
        }
    },
}
</script>
<style scoped>

</style>