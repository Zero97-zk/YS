<template>
    <header class="clearfix">
        <div class="text-white mx-0 open clearfix">
            <div class="float-left ml-1"><span class="glyphicon glyphicon-folder-close" @click="app_to_down"></span></div>
            <div class="avatar float-right mr-4" v-show="is_logged"><img :src="avatar_url" alt="avatar"></div>
            <div class="float-right mr-4" @click="go_register"><span>{{register_or_logout()}}</span></div>
            <div class="float-right mr-2" @click="go_login"><span>{{login_or_nickname()}}</span></div>
        </div>
        <div id="apps" :style="{top:top}">
            <div class="app_close"><span class="glyphicon glyphicon-folder-open " @click="app_to_up"></span></div>
            <div class="app_body">
                <ul class="row list-unstyled">
                    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-2 text-center mt16 cursor_pointer" @click="to_selfinfo">
                        <img src="../../static/img/1187084.png" alt="个人中心" title="个人中心">
                        <p class="text-center">个人中心</p>
                    </li>
                    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-2 text-center mt16 cursor_pointer" @click="to_conclusion">
                        <img src="../../static/img/1121851.png" alt="文档管理" title="文档管理">
                        <p class="text-center">总结管理</p>
                    </li>
                    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-2 text-center mt16 cursor_pointer" @click="to_todo">
                        <img src="../../static/img/1187092.png" alt="待办事项" title="待办事项">
                        <p class="text-center">行动日志</p>
                    </li>
                </ul>
            </div>
        </div>
    </header>
</template>
<script>
import '../assets/css/common.css'

export default {
    name: "Header",
    data(){
        return {
            top:"-70%",
            is_logged: false,
            user_id: null,
            nickname:"",
            avatar_url: "",
        }
    },
    methods:{
        app_to_up(){
            this.top = "-70%";
        },
        app_to_down(){
            this.top = 0;
        },
        login_or_nickname(){
            return this.is_logged?this.nickname:"登录";
        },
        register_or_logout(){
            return this.is_logged?"登出":"注册"
        },
        go_login(){
            if (this.is_logged==false){
                this.$router.push("/")
            }
        },
        go_register(){
            if (this.is_logged==false){
                this.$router.push("/")
            }else{
                localStorage.removeItem("ytoken");
                localStorage.removeItem("user_id");
                this.is_logged = false;
                this.$router.push("/")
            }
        },
        to_selfinfo(){
            this.app_to_up();
            var user_id = localStorage.getItem("user_id");
            if(user_id){
                this.$router.push({path:'/userinfo', query:{user_id:user_id}})
            }else{
                var to_login = confirm('登录后才可以进入个人中心，是否选择先去登录?');
                if (to_login){
                    this.$router.push({name:'Index'})
                }
            }
        },
        to_conclusion(){
            this.app_to_up();
            var user_id = localStorage.getItem("user_id");
            if(user_id){
                this.$router.push({name:'Personal',query:{personal_id:user_id}})
            }else{
                this.$router.push({name:'Forum'})
            }
        },
        to_todo(){
            this.app_to_up();
            var user_id = localStorage.getItem("user_id");
            if(user_id){
                this.$router.push({path:'/todo'})
            }else{
                var to_login = confirm('登录后才可以进入行动日志，是否选择先去登录?');
                if (to_login){
                    this.$router.push({name:'Index'})
                }
            }
        }
    },
    created(){
        var ytoken = localStorage.getItem('ytoken');
        var user_id = localStorage.getItem('user_id');
        if (ytoken){
            this.axios.get(this.axios.defaults.baseURL+"api/v1/users/"+user_id).then(result=>{
                if (result.data.code==200){
                    this.is_logged = true;
                    this.user_id = user_id;
                    this.nickname = result.data.data.nickname;
                    if (!result.data.data.avatar){
                        this.avatar_url = "../../static/img/avatar.png";
                    }else{
                        this.avatar_url = this.axios.defaults.baseURL+"static_backend/"+result.data.data.avatar;
                    }
                }else{
                    alert(result.data.error);
                }
            })
        }
    }
}
</script>