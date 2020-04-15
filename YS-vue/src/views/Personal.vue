<template>
    <div id="personal">
        <div class="container clearfix px-0">
            <div class="con_l float-left">
                <div class="outer_box">
                    <div class="inner_box con_l_inner_box">
                        <div class="content_box">
                            <ul class="tags list-unstyled" style="color:#fff;font-weight:500;font-size:14px">
                                <li style="margin-bottom: 15px">
                                    <h5>
                                    <span class="glyphicon glyphicon-cog"></span>
                                    <span>标签</span>
                                    </h5>
                                </li>
                                <li class="tag_li clearfix p-2 bg_dark_hover cursor_pointer" :class="tag_select_bg(`all`)" @click="select_display()">
                                    <span class="tag_content float-left">全部</span>
                                    <span class="tag_article_count float-right">{{all_articles.length}}</span>
                                </li>
                                <li class="tag_li clearfix p-2 bg_dark_hover cursor_pointer" v-for="(tag, tag_i) of tag_list" :key="tag_i" :class="tag_select_bg(tag.tag)" @click="select_display(tag)">
                                    <span class="tag_content float-left">{{tag.tag}}</span>
                                    <span class="tag_article_count float-right">{{tag.data.length}}</span>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="con_m float-left">
                <div class="outer_box">
                    <div class="inner_box">
                        <div class="content_box">
                            <ul class="articles_synopsis list-unstyled" style="margin-top:10px">
                                <li class="synopsis_li shadow_light_hover cursor_pointer" v-for="(article, art_i) of display_articles" :key="art_i" @click="to_article(article)">
                                    <div class="synopsis_title">
                                        <h4>{{article.title}}</h4>
                                    </div>
                                    <div class="synopsis_introduce">
                                        <p style="margin-bottom: 5px">{{article.introduce}}</p>
                                    </div>
                                    <div class="synopsis_other_info clearfix cursor_pointer">
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
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="con_r float-left">
                <div class="outer_box">
                    <div class="inner_box" style="width: 106.5%;">
                        <div class="content_box">
                            <div class="personal_info">
                                <div style="height:50%;">
                                    <img src="../../static/img/index_bg3.jpg" alt="" style="width:100%;height:100%">
                                </div>
                                <div class="personal_avatar">
                                    <img :src="personal_avatar_url" alt="" style="width:100%;height:100%;border-radius:50%;">
                                </div>
                                <div class="personal_nickname text-center" style="font-size:15px;font-weight:500;margin-top:33px">
                                    <span>{{personal_nickname}}</span>
                                </div>
                                <div class="personal_phone pt-1 text-center" style="font-size:14px;color:#555">
                                    <span class="glyphicon glyphicon-phone-alt"></span>
                                    <span> {{personal_phone}}</span>
                                </div>
                                <div class="personal_email pt-1 text-center" style="font-size:14px;color:#555">
                                    <span class="glyphicon glyphicon-envelope"></span>
                                    <span> {{personal_email}}</span>
                                </div>
                            </div>
                            <div class="hot_articles">
                                <h5>
                                    <span class="glyphicon glyphicon-fire"></span>
                                    <span style="font-weight: bold;">热门总结</span>
                                </h5>
                                <ul class="list-unstyled">
                                    <li v-for="(hot, hot_i) of hot_articles" :key="hot_i">
                                        <p class="mb-0 cursor_pointer text_deepblue_hover" @click="to_article(hot)">{{hot.title}}</p>
                                        <div style="color:#888;font-size:14px;margin-top:-4px;">
                                            <span class="glyphicon glyphicon-eye-open"></span>
                                            <span> {{hot.watch_count}}</span>
                                        </div>
                                    </li>
                                    <li></li>
                                </ul>
                            </div>
                            <div class="beian mt-2 p-2 bg-white text-center">
                                <a href="http://www.beian.miit.gov.cn" target="_blank" class="text-dark text-decoration-none" style="font-size:14px;color:#666;">鄂ICP备200002048</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import "../assets/css/common.css"
import {getUserInfo,getAuthorArticles} from "../assets/js/apis/article"

export default {
    name: "Personal",
    data(){
        return {
            tag: "all",
            tag_list: [],
            personal_id: null,
            personal_avatar_url:"",
            personal_nickname: "",
            personal_phone: "",
            personal_email: "",
            hot_articles: [],
            display_articles: [],
            all_articles:[]
            
        }
    },
    methods:{
        tag_select_bg(select){
           if (select==this.tag){
               return 'bg_dark'
           } 
        },
        get_imgurl(url){
            if (!url){
                return "../../static/img/index_bg.jpg"
            }else{
                return this.axios.defaults.baseURL+"static/"+url
            }
        },
        select_display(tag=null){
            if (tag){
                this.tag = tag.tag;
                this.display_articles = tag.data;
            }else{
                this.tag = "all",
                this.display_articles = this.all_articles;
            }
        },
        to_article(article){
            var {href} = this.$router.resolve({path: '/article', query:{author_id:this.personal_id, article_id:article.id}});
            window.open(href, '_blank');
        }
    },
    created(){
        var personal_id = this.$route.query.personal_id;
        this.personal_id = parseInt(personal_id);
        getUserInfo(this.personal_id).then(result=>{
            if (result.code==200){
                this.personal_avatar_url = this.get_imgurl(result.data.avatar);
                this.personal_nickname = result.data.nickname;
                this.personal_phone = result.data.phone;
                this.personal_email = result.data.email;
            }else{
                alert(result.error);
            }
        });
        getAuthorArticles(this.personal_id).then(result=>{
            if (result.code==200){
                this.all_articles = result.data;
                this.display_articles = this.all_articles;
                this.hot_articles = this.all_articles.sort((a,b)=>{
                    return b.watch_count - a.watch_count
                }).slice(0, 10);
                this.tag_list = result.tag_data;
            }else{
                alert(result.error)
            }
        })
        
    }
}
</script>
<style scoped>
#personal{
    width: 100%;
    height: 100%;
    /* background-image: linear-gradient(to bottom, #72afd5, #72afd5, #b0d7ee); */
    background:#72afd5;
}
#personal>.container{
    max-width: 1250px !important;
    height:100%;
    background: rgba(255, 255, 255, 0.2);
    /* box-shadow: 0 0 3px 0; */
}
.con_l{
    width: 160px;
    height: 100%;
}
.con_m{
    width: 820px;
    height: 100%;
}
.con_r{
    width: 270px;
    height: 100%;
}
.con_l_inner_box{
    width: 115%;
}
.tags{
    margin-top: 20px;
}
.tag_article_count{
    background: #ed741c;
    padding: 0 8px;
    font-size: 13px;
    border-top-right-radius: 50%;
    border-top-left-radius: 50%;
    border-bottom-left-radius: 50%;
}
.synopsis_li{
    background: #fff;
    border-radius: 3px;
    margin-right: 24px;
    padding: 8px 16px;
    margin-bottom: 10px;
}
.synopsis_title>h4{
    font-weight:550
}
.synopsis_introduce{
    font-size:14px;
    color: #444;
}
.synopsis_other_info{
    font-size:14px;
    color: #444;
}
.personal_info{
    position: relative;
    width: 250px;
    height: 230px;
    background: #fff;
}
.personal_avatar{
    position: absolute;
    left: 95px;
    top: 85px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    box-shadow: 0 0 5px 0 #fff;
}
.hot_articles{
    margin: 10px auto;
    padding: 10px;
    background: #fff;
}
</style>