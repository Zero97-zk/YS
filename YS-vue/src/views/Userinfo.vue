<template>
    <div id="userinfo">
        <my-header/>
        <div class="inner_window" :style="{top:inner_window_top}">
            <div class="c_box avatar_upload_box" v-show="inner_window_content=='avatar upload'">
                <div class="avatar_upload">
                    <label for="avatar_upload">
                        <span class="glyphicon glyphicon-cloud-upload text_deepblue cursor_pointer float-left"></span>
                    </label>
                    <input type="file" accept="image/png,image/jpeg,image/gif" id="avatar_upload" style="display:none" @change="get_file">
                </div>
                <div style="font-size:14px;color:#666;cursor:default">
                    仅支持jpg、png、gif格式
                </div>
                <div style="width:100px;height:100px;margin:10px auto;">
                    <img src="" alt="" id='preview_img' style="border-radius:50%;">
                </div>
                <div style="margin-top:20px;">
                    <button class="b_btn" style="mrigin-right:15px" @click="update_avatar">上传</button>
                    <button class="b_btn" style="margin-left:15px" @click="close_inner_window">取消</button>
                </div>
            </div>
            <div class="c_box edit_info_box text-center" v-show="inner_window_content=='edit info'">
                <div class="edit_content">
                     <div class="editor text_deepblue">
                        <span class="glyphicon glyphicon-edit"></span>
                        <span>编辑个人信息</span>
                    </div>
                    <div class="edit_nickname">
                        <label for="edit_nickname">昵称</label>
                        <input type="text" id="edit_nickname" class="form-control" :placeholder="nickname_ph">
                    </div>
                    <div class="edit_phone">
                        <label for="edit_phone">手机号码</label>
                        <input type="text" id="edit_phone" class="form-control" :placeholder="phone_ph">
                    </div>
                    <div class="edit_email">
                        <label for="edit_email">邮箱</label>
                        <input type="email" id="edit_email" class="form-control" :placeholder="emil_ph">
                    </div>
                    <div class="edit_description">
                        <label for="edit_description">个人描述</label>
                        <textarea id="edit_description" rows="3" class="form-control" :placeholder="description_ph"></textarea>
                    </div>
                </div>
                <div>
                    <button class="b_btn" style="margin-right:15px;border-color:red;" @click="put_user_info">提交</button>
                    <button class="b_btn" style="margin-left:15px;border-color:red;" @click="close_inner_window">取消</button>
                </div>
            </div>
        </div>
        <div class="ui_container clearfix">
            <div class="nav_box float-left">
                <ul class="list-unstyled" @click="chose_nav">
                    <li class="nav_li" :class="nav_choose('my_info')"><span>个人信息</span></li>
                    <li class="nav_li" :class="nav_choose('my_collection')"><span>我的收藏</span></li>
                    <li class="nav_li" :class="nav_choose('my_attention')"><span>我的关注</span></li>
                    <li class="nav_li" :class="nav_choose('my_fans')"><span>我的粉丝</span></li>
                </ul>
            </div>
            <div class="display_box float-left">
                <div class="outer_box">
                    <div class="inner_box" style="width:102%;">
                        <div class="content_box">
                            <div class="my_info_box" v-show="nav_select=='my_info'">
                                <div class="info_t clearfix">
                                    <span style="font-weight: bold;font-size: 1.5rem;">个人信息</span>
                                    <hr>
                                </div>
                                <div class="info_m clearfix">
                                    <div class="avatar_box">
                                        <img :src="avatar" alt="" style="border-radius:50%">
                                        <span class="text_deepblue cursor_pointer" style="margin-left:11px;" @click="open_avatar_upload">更换头像</span>
                                    </div>
                                    <div class="name_info">
                                        <div class="detail_info" style="height:25px;top:0">
                                            <span>用户:</span>
                                            <span style="margin-left:5px;">{{username}}</span>
                                        </div>
                                        <div class="detail_info" style="height:25px;top:25px;">
                                            <span>昵称:</span>
                                            <span style="margin-left:5px;">{{nickname}}</span>
                                        </div>
                                        <div class="detail_info" style="height:25px;top:50px;">
                                            <span>关注:</span>
                                            <span style="margin-left:5px;">{{attention_count}}</span>
                                        </div>
                                        <div class="detail_info" style="height:25px;top:75px">
                                            <span>粉丝:</span>
                                            <span style="margin-left:5px;">{{fans_count}}</span>
                                        </div>
                                    </div>
                                    <div class="float-right mr-5" style="height:100px;line-height:100px">
                                        <span class="text_deepblue cursor_pointer" @click="to_personal_conclusion(user_id)">个人总结页-></span>
                                    </div>
                                </div>
                                <hr>
                                <div class="info_b clearfix mt-5">
                                    <div class="editor text_deepblue cursor_pointer float-right mr-5" @click="edit_self_info">
                                        <span class="glyphicon glyphicon-edit"></span>
                                        <span>编辑个人信息</span>
                                    </div>
                                    <div class="others_info">
                                        <div class="phone text-center p-2">
                                            <span class="glyphicon glyphicon-phone-alt"></span>
                                            <span> {{phone}}</span>
                                        </div>
                                        <div class="email text-center p-2">
                                            <span class="glyphicon glyphicon-envelope"></span>
                                            <span> {{email}}</span>
                                        </div>
                                        <div class="description text-center p-2">
                                            <span>个人描述:</span>
                                            <span class="ml-2">{{description}}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="my_collection_box" v-show="nav_select=='my_collection'">
                                 <div class="info_t clearfix">
                                    <span style="font-weight: bold;font-size: 1.5rem;">总结收藏</span>
                                    <span class="float-right collect_count">{{collect_count}}</span>
                                    <hr>
                                </div>
                                <div class="collect_box">
                                    <ul class="list-unstyled">
                                        <li class="text-center" style="height:80px;line-height:80px" v-show="!collect_count">
                                            <span style="font-size:2rem;font-weight:blod">空空如也-(0.0)-</span>
                                        </li>
                                        <li class="collect_li shadow_light_hover" v-for="(article, art_i) of collection_list" :key="art_i">
                                            <span class="remove_collect cursor_pointer" @click="del_collection(article.id)">×</span>
                                            <div class="article_title">
                                                <h5 @click="to_article(article)" class="cursor_pointer text_red_hover">{{article.title}}</h5>
                                            </div>
                                            <div class="article_other_info clearfix">
                                                <div class="float-left cursor_pointer" style="width:30px;height:30px" @click="to_personal_conclusion(article.author_id)">
                                                    <img :src="get_imgurl(article.author_avatar)" alt="" style="width:100%;height:100%;border-radius:50%;">
                                                </div>
                                                <div class="float-left ml-2 pt-1 cursor_pointer" style="font-weight:500;" @click="to_personal_conclusion(article.author_id)">
                                                    <span class="text_deepblue">{{article.author_name}}</span>
                                                </div>
                                                <div class="float-right">
                                                    <span class="glyphicon glyphicon-comment text_deepblue_hover"></span>
                                                    <span class="text_deepblue">{{article.message_count}}</span>
                                                </div>
                                                <div class="float-right mr-3">
                                                    <span class="glyphicon glyphicon-heart-empty text_deepblue_hover"></span>
                                                    <span class="text_deepblue">{{article.like_count}}</span>
                                                </div>
                                                <div class="float-right mr-3">
                                                    <span class="glyphicon glyphicon-eye-open text_deepblue_hover"></span>
                                                    <span class="text_deepblue">{{article.watch_count}}</span>
                                                </div>
                                                <div class="float-right mr-3">
                                                    <span class="glyphicon glyphicon-time"></span>
                                                    <span>{{article.created_time}}</span>
                                                </div>                                                                                                                        
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="my_attention_box" v-show="nav_select=='my_attention'">
                                <div class="info_t clearfix">
                                    <span style="font-weight: bold;font-size: 1.5rem;">我关注的用户</span>
                                    <span class="float-right attention_count">{{attention_count}}</span>
                                    <hr>
                                </div>
                                <div class="attention_box">
                                    <ul class="list-unstyled">
                                        <li class="text-center" style="height:80px;line-height:80px" v-show="!attention_count">
                                            <span style="font-size:2rem;font-weight:blod">空空如也-(0.0)-</span>
                                        </li>
                                        <li class="attention_li clearfix" v-for="(at_user, at_id) of attention_list" :key="at_id">
                                            <div class="user_avatar float-left cursor_pointer" style="width:48px;height:48px;" @click="to_personal_conclusion(at_user.id)">
                                                <img :src="get_imgurl(at_user.avatar)" alt="" style="border-radius:50%;">
                                            </div>
                                            <div class="user_name float-left ml-3" style="line-height:48px;font-weight:500;color:#3399ea"  @click="to_personal_conclusion(at_user.id)">
                                                <span class="cursor_pointer"> {{at_user.nickname}}</span>
                                            </div>
                                            <div class="float-right">
                                                <button class="float-right remove_attention_btn" @click="del_follow(at_user.id)">取消关注</button>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="my_fans_box" v-show="nav_select=='my_fans'">
                                <div class="info_t clearfix">
                                    <span style="font-weight: bold;font-size: 1.5rem;">关注我的用户</span>
                                    <span class="float-right attention_count">{{fans_count}}</span>
                                    <hr>
                                </div>
                                <div class="fans_box">
                                    <ul class="list-unstyled">
                                        <li class="text-center" style="height:80px;line-height:80px" v-show="!fans_count">
                                            <span style="font-size:2rem;font-weight:blod">空空如也-(0.0)-</span>
                                        </li>
                                        <li class="attention_li clearfix" v-for="(fan, f_id) of fans_list" :key="f_id">
                                            <div class="user_avatar float-left cursor_pointer" style="width:48px;height:48px;"  @click="to_personal_conclusion(fan.id)">
                                                <img :src="get_imgurl(fan.avatar)" alt="" style="border-radius:50%">
                                            </div>
                                            <div class="user_name float-left ml-3" style="line-height:48px;font-weight:500;color:#3399ea"  @click="to_personal_conclusion(fan.id)">
                                                <span class="cursor_pointer"> {{fan.nickname}}</span>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="beian">
                <a href="http://www.beian.miit.gov.cn" target="_blank" class="text-dark text-decoration-none" style="font-size:14px;color:#666;">鄂ICP备200002048</a>
            </div>
        </div>
    </div>
</template>
<script>
import "../assets/css/common.css"

import {getUserInfo,getFans,deleteFollow,getCollections,deleteCollection} from '../assets/js/apis/article'
import {getFollow,createAvatar,putUserInfo} from '../assets/js/apis/userinfo'

export default {
    name: 'Userinfo',
    data(){
        return {
            nav_select:"my_info",
            user_id: localStorage.getItem('user_id'),
            avatar: null,
            username: null,
            nickname: null,
            phone: null,
            email: null,
            description: null,
            collect_count: null,
            attention_count: null,
            fans_count: null,
            collection_list: [],
            attention_list: [],
            fans_list: [],
            inner_window_top: "-100%",
            inner_window_content: null,
            nickname_ph: "",
            phone_ph: '',
            emil_ph: '',
            description_ph: ''
        }
    },
    methods:{
        open_inner_window(){
            this.inner_window_top = "0"
        },
        close_inner_window(){
            this.inner_window_top = "-100%"
        },
        open_avatar_upload(){
            this.inner_window_content = 'avatar upload';
            document.getElementById('preview_img').setAttribute('src', this.avatar)
            this.open_inner_window();
        },
        edit_self_info(){
            this.inner_window_content = 'edit info';
            this.open_inner_window();
        },
        nav_choose(select){
            if (this.nav_select==select){
                return "nav_chose"
            }
        },
        chose_nav(e){
            switch (e.target.textContent){
                case '个人信息':
                    this.nav_select = "my_info";
                    break;
                case '我的收藏':
                    this.nav_select = 'my_collection';
                    break;
                case '我的关注':
                    this.nav_select = 'my_attention';
                    break;
                case '我的粉丝':
                    this.nav_select = 'my_fans';
                    break;
            };
        },
        get_file(e){
            var file = e.target.files[0];
            var preview_img = document.getElementById('preview_img');
            var file_render = new FileReader();
            file_render.readAsDataURL(file);
            file_render.onload = function(e){
                preview_img.setAttribute('src', e.target.result)
            }
        },
        get_imgurl(url){
            if (!url){
                return "../../static/img/avatar.png"
            }else{
                return this.axios.defaults.baseURL+"static/"+url
            }
        },
        get_user_info(){
            getUserInfo(this.user_id).then(result=>{
                if (result.code==200){
                    this.avatar = this.get_imgurl(result.data.avatar);
                    this.username = result.data.username;
                    this.nickname = result.data.nickname;
                    this.phone = result.data.phone;
                    this.email = result.data.email;
                    this.description = result.data.description;
                    this.nickname_ph = result.data.nickname;
                    this.phone_ph = result.data.phone;
                    this.emil_ph = result.data.email;
                    this.description_ph = result.data.description;
                }else{
                    alert(result.error)
                }
            })
        },
        get_fans(){
            getFans(this.user_id).then(result=>{
                if (result.code==200){
                    this.fans_count = result.detail_data.length;
                    this.fans_list = result.detail_data;
                }else{
                    alert(result.error)
                }
            })
        },
        get_follow(){
            getFollow(this.user_id).then(result=>{
                if (result.code==200){
                    this.attention_count = result.detail_data.length;
                    this.attention_list = result.detail_data
                }else{
                    alert(result.error)
                }
            })
        },
        del_follow(followed_id){
            deleteFollow(followed_id).then(result=>{
                if (result.code==200){
                   this.get_follow();
                }else if(result.code==10202){
                    alert('会话已过期,请重新登陆');
                    localStorage.removeItem('ytoken');
                    localStorage.removeItem('user_id');
                    this.$router.push({name:'Index'})
                }else{
                    alert(result.error)
                }
            });

        },
        get_collections(){
            getCollections(this.user_id).then(result=>{
                if (result.code==200){
                    this.collect_count = result.data.length;
                    this.collection_list = result.data
                }else{
                    alert(result.error)
                }
            })
        },
        del_collection(collected_id){
            deleteCollection(collected_id).then(result=>{
                if (result.code==200){
                    this.get_collections();
                }else if(result.code==10202){
                    alert('会话已过期,请重新登陆');
                    localStorage.removeItem('ytoken');
                    localStorage.removeItem('user_id');
                    this.$router.push({name:'Index'})
                }else{
                    alert(result.error)
                }
            })
        },
        to_personal_conclusion(personal_id){
            this.$router.push({name:'Personal', query:{personal_id}})
        },
        to_article(article){
            var {href} = this.$router.resolve({path: '/article', query:{author_id:article.author_id, article_id:article.id}});
            window.open(href, '_blank');
        },
        update_avatar(){
            var file = document.getElementById('avatar_upload').files[0];
            var formdata = new FormData();
            formdata.append('avatar', file);
            createAvatar(this.user_id,formdata).then(result=>{
                if (result.code==200){
                    this.get_user_info();
                    this.close_inner_window()
                }else if(result.code==10202){
                    alert('会话已过期,请重新登陆');
                    localStorage.removeItem('ytoken');
                    localStorage.removeItem('user_id');
                    this.$router.push({name:'Index'})
                }else{
                    alert(result.error)
                }
            })
        },
        put_user_info(){
            var p_nickname = document.getElementById('edit_nickname').value;
            var p_phone = document.getElementById('edit_phone').value;
            var p_email = document.getElementById('edit_email').value;
            var p_description = document.getElementById('edit_description').value;
            var data = {};
            if (p_nickname){
                data.nickname = p_nickname
            };
            if (p_phone){
                data.phone = p_phone
            };
            if (p_email){
                data.email = p_email
            };
            if (p_description){
                data.description = p_description
            };
            putUserInfo(this.user_id,data).then(result=>{
                if (result.code==200){
                     this.get_user_info();
                    this.close_inner_window();
                }else if(result.code==10202){
                    alert('会话已过期,请重新登陆');
                    localStorage.removeItem('ytoken');
                    localStorage.removeItem('user_id');
                    this.$router.push({name:'Index'})
                }else{
                    alert(result.error)
                }
            })
        }
    },
    created(){
        this.get_user_info();
        this.get_fans();
        this.get_follow();
        this.get_collections();
    }    
}
</script>
<style scoped>
#userinfo .beian{
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 40px;
    line-height: 40px;
    margin-left: 20px;
}
#userinfo{
    width:100%;
    height: 100%;
    background: #b0d7ee;
}
.ui_container{
    position: relative;
    width: 1250px;
    height: 100%;
    padding: 50px 20px;
    margin: 0 auto;
    background: rgba(255, 255, 255, 0.2);
    
}
.ui_container>.nav_box{
    width:210px;
    /* height: 400px; */
    background: rgba(255, 255, 255, 0.2);
    padding: 10px 0;
}
.nav_box .nav_li{
    height: 36px;
    line-height: 36px;
    padding-left: 20px;
    font-size: 15px;
    color: #666;
}
.nav_box .nav_li:hover{
    background: rgba(0, 0, 0, 0.4);
    color: #fff;
    cursor: pointer;
}
.display_box{
    width: 950px;
    height: 100%;
    margin-left: 40px;
    background:rgba(255, 255, 255, 0.2);
}
.my_info_box{
    height: 100%;
    background-image: linear-gradient(-45deg, #d0f7ee, #f0d7ee);
    background-size: 100% 100%;
    color: #455;
}
.info_t{
    padding-top: 30px;
    padding-left:20px; 
}
.info_m{
    height:100px;
    font-size: 15px;
    margin-top: 10px;
}
.avatar_box{
    float: left;
    width:80px;
    height:80px;
    margin-left: 30px;
    /* margin-top: 10px; */
}
.name_info{
    float: left;
    width: 400px;
    height: 100px;
    margin-left:20px;
    position: relative;
}
.detail_info{
    position:absolute;
    left:20px;
    /* top:20px; */
}
.info_b{
    position: relative;
}
.others_info{
    position: absolute;
    top: 40px;
    width: 100%;
    height: 100%;
    font-size: 15px;
    /* color: #555; */
}
.collect_box{
    height: 100%;
    margin-left:20px;
}
.collect_count{
    padding: 2px 14px;
    background: #3399ea;
    color: #fff;
    margin-right:10px;
    margin-top: 10px;
    border-top-right-radius: 50%;
    border-top-left-radius: 50%;
    border-bottom-left-radius: 50%;
}
.collect_li{
    position: relative;
    background: #fff;
    border-radius: 3px;
    margin-right: 24px;
    padding: 8px 16px;
    margin-bottom: 10px;
}
.article_title>h5{
    font-weight:550
}
.article_other_info{
    font-size:14px;
    color: #444;
}
.remove_collect{
    position: absolute;
    right: 3px;
    top: -4px;
    color: #666;
    font-size:18px;
}
.remove_collect:hover{
    transform: scale(1.5);
}
.attention_count{
    padding: 2px 14px;
    background: #343a40;
    color: #fff;
    margin-right:10px;
    margin-top: 10px;
    border-top-right-radius: 50%;
    border-top-left-radius: 50%;
    border-bottom-left-radius: 50%;
}
.attention_box{
    height:100%;
    margin-left: 20px;
}
.attention_li{
    height: 82px;
    padding: 16px 16px;
    margin-right: 24px;
    /* margin-bottom:10px; */
    border-top: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
}
.attention_li+.attention_li{
    height:81px;
    border-top:0;
}
.remove_attention_btn{
    margin-top:3px;
    width: 100px;
    height: 40px;
    border-radius: 3px;
    border: 1px solid #aaa;
    color: #666;
}
.remove_attention_btn:hover{
    color: #fff;
    background: #3399ea;
    border: 1px solid#3399ea;
}
.fans_box{
    height:100%;
    margin-left: 20px;
}
.nav_chose{
    background:rgba(0, 0, 0, 0.6);
    color:#fff !important;
}
.inner_window{
    position: absolute;
    width: 100%;
    height: 100%;
    left: 0;
    z-index: 999;
    background: rgba(0, 0, 0, 0.2);
    transition: all 0.25s;
}
.c_box{
    position: absolute;
    width: 24%;
    left:38%;
    top:100px;
    background: #fff;
    border-radius: 5px;
}
.avatar_upload_box{
    height: 300px;
    text-align: center
}
.avatar_upload{
    margin-top:60px;
    font-size:18px;
}
.b_btn{
    font-size: 15px;
    padding: 3px 15px;
    background: #fff;
    border: 1px solid #666;
    color: #666;
    border-radius: 3px;
}
.b_btn:hover{
    color: #fff;
    background: red;
    border: 1px solid red;
}
.edit_info_box{
    height: 500px;
}
.edit_content{
    font-size: 15px;
    color: #666;
    padding: 30px;
}
.edit_content>div+div{
    margin-top:10px;
}
</style>