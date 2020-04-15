<template>
    <div id='main' class="clearfix">
       <!-- <my-header></my-header> -->
        <div id="logo">
            <img src="../../static/img/logo1.jpg" alt="">
        </div>
        <div id="content" class="row">
            <div class="col-md-4 col-sm-12 offset-md-2 c_left">
                <div class="l_head">
                    <p class="mb-0">欢迎,</p>
                    <p>来到青年小栈</p>
                </div>
                <p class="l_middle">这是一个辅助年轻人自我管理的网站,如果你想知道这个网站有什么功能，你可以试着点击以下按钮</p>
                <button class="btn btn-lg border-info l_foot" @click="to_md">功能介绍页 <span class="glyphicon glyphicon-arrow-right"></span></button>
                <button class="btn btn-lg border-info l_foot" @click="to_forum">总结论坛页 <span class="glyphicon glyphicon-arrow-right"></span></button>
                <p class="l_tip text-warning">提示:网站中几乎所有的功能都是只提供给用户</p>
            </div>
            <div class="col-md-3 offset-md-2 c_right">
                <div v-show="show" style="height:23rem" class="form" :class="translate">
                    <button class="btn float-right" @click="login_register_convert">注册<span class="glyphicon glyphicon-hand-right"></span></button>
                    <p class="text-center">登录</p>
                    <hr>
                    <div class="form-group mt-1 mb-0">
                        <span class="glyphicon glyphicon-user"></span>
                        <label for="username">用户名</label>
                        <input type="text" class="form-control" id="username" name="username" placeholder="请输入用户名">
                    </div>
                    <div>
                        <p class="text-danger error"></p>
                    </div>
                    <div class="form-group mb-0">
                        <span class="glyphicon glyphicon-lock"></span>
                        <label for="password">密码</label>
                        <input type="password" class="form-control" id="password" name="password" placeholder="请输入密码">
                    </div>
                    <div>
                        <p class="text-danger error"></p>
                    </div>
                    <div class="form-group">
                        <label class="avoid_login">
                            <input type="checkbox" id="avoid_login"> 记住我
                        </label>
                    </div>
                    <div>
                        <button id="register" class="btn btn-block submit" @click="index_login">登录</button>
                    </div>
                </div>
                <div v-show="!show" class="form" :class="translate">
                    <button class="btn float-left" @click="login_register_convert"><span class="glyphicon glyphicon-hand-left">登录</span></button>
                    <p class="text-center mb-0">注册</p>
                    <div class="form-group mt-1 mb-0">
                        <span class="glyphicon glyphicon-user"></span>
                        <label for="reg_username">用户名</label>
                        <input type="text" class="form-control" id="reg_username" name="reg_username" placeholder="请输入用户名">
                    </div>
                    <div>
                        <p class="text-danger error"></p>
                    </div>
                    <div class="form-group mb-0">
                        <span class="glyphicon glyphicon-lock"></span>
                        <label for="reg_password">密码</label>
                        <input type="password" class="form-control" id="reg_password" name="reg_password" placeholder="请输入密码">
                    </div>
                    <div>
                        <p class="text-danger error"></p>
                    </div>
                    <div class="form-group mt-1 mb-0">
                        <span class="glyphicon glyphicon-send"></span>
                        <label for="email">邮箱</label>
                        <input type="email" class="form-control" id="email" name="email" placeholder="请输入邮箱">
                    </div>
                    <div>
                        <p class="text-danger error"></p>
                    </div>
                    <div class="form-group mb-0">
                        <span class="glyphicon glyphicon-phone"></span>
                        <label for="phone">手机</label>
                        <input type="text" class="form-control" id="phone" name="phone" placeholder="请输入手机号码">
                    </div>
                    <div>
                        <p class="text-danger error"></p>
                    </div>
                    <div>
                        <button id="login" class="btn btn-block submit" @click="index_register">注册</button>
                    </div>
                </div>
            </div>
        </div>
        <my-footer></my-footer>
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
        index_login(){
            var username  = document.getElementById("username").value;
            var password = document.getElementById("password").value;
            var avoid_login = document.getElementById("avoid_login").checked;
            var data = {
                username: username,
                password: password,
                avoid_login: avoid_login
            };
            login(data).then(result=>{
                if (result.code==200){
                    localStorage.setItem('ytoken', result.token);
                    localStorage.setItem('user_id', result.id)
                    this.$router.push("/todo")
                }else{
                    alert(result.error)
                }
            })
        },
        index_register(){
            var username = document.getElementById("reg_username").value;
            var password = document.getElementById("reg_password").value;
            var email = document.getElementById("email").value;
            var phone = document.getElementById("phone").value;
            var data = {
                username: username,
                password: password,
                email: email,
                phone: phone
            };
            register(data).then(result=>{
                if (result.code==200){
                    localStorage.setItem('ytoken', result.token);
                    localStorage.setItem('user_id', result.id)
                    this.$router.push("/todo");
                }else{
                    alert(result.error)
                }
            })
        },
        to_md(){
            this.$router.push({name:"Md"});
        },
        to_forum(){
            this.$router.push({name:'Forum'})
        }
    },
    created(){
        var ytoken = window.localStorage.getItem('ytoken');
        if (ytoken) {
            avoidLogin(ytoken).then(
                result=>{
                    if (result.code==200){
                        this.$router.push("/todo");
                    }
                }
            )
        }
    }
}
</script>
<style scoped>

</style>