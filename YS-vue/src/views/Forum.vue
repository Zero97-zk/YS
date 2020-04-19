<template>
    <div id="forum" class="bg-white">
        <div class="container clearfix">
            <div class="c_l float-left">
                <div class="search_box text-center pt-3" style="height:7%;position:relative">
                    <div class="search">
                        <input type="text" id="search" placeholder="请输入相关搜索" v-model="search_text">
                        <div class="search_ico">
                            <span class="glyphicon glyphicon-search"></span>
                        </div>
                    </div>
                    <div class="topic_type" v-show="search_condition">
                        <span class="float-right glyphicon glyphicon-remove cursor_pointer text_deepblue_hover" style="top:1px;right:-7px;color:rgba(0,0,0,0.4)" @click="remove_tag"></span>
                        <span>{{search_condition}}</span>
                        <span>{{condition_text.slice(0,10)+'...'}}</span>
                        <span class="float-right display_count">{{condition_articles_count}}</span>
                    </div>
                    <ul class="list-unstyled search_select text-left" v-show="search_text.length">
                        <li class="px-3 py-1 bg_deepblue_hover cursor_default clearfix" @click="get_tag_articles">
                            <span class="float-left">{{search_text}}</span>
                            <span class="float-left ml-5">搜索标签</span>
                        </li>
                        <li class="px-3 py-1 bg_deepblue_hover cursor_default clearfix" @click="get_author_articles">
                            <span class="float-left">{{search_text}}</span>
                            <span class="float-left ml-5">搜索作者</span>
                        </li>
                        <li class="px-3 py-1 bg_deepblue_hover cursor_default clearfix" @click="get_title_articles">
                            <span class="float-left">{{search_text}}</span>
                            <span class="float-left ml-5">搜索标题</span>
                        </li>
                    </ul> 
                </div>
                <div class="articles_box" style="height:93%;padding-top:10px;">
                    <div class="outer_box">
                        <div class="inner_box" style="padding-right:25px;">
                            <div class="content_box">
                                <ul class="article_synopsis list-unstyled">
                                    <li class="text-center" style="height:80px;line-height:80px" v-show="!display_articles.length" >
                                        <span style="font-size:2rem;font-weight:blod">没有找到相关总结-(0.0)-</span>
                                    </li>
                                    <li class="synopsis_li shadow_light_hover cursor_pointer" v-for="(article, art_i) of display_articles" :key="art_i" @click="to_article(article.id,article.author_id)">
                                        <div class="synopsis_title">
                                            <h4>{{article.title}}</h4>
                                        </div>
                                        <div class="synopsis_introduce">
                                            <p style="margin-bottom: 5px">{{article.introduce}}</p>
                                        </div>
                                        <div class="synopsis_other_info clearfix cursor_pointer">
                                            <div class="float-left" style="width:30px;height:30px">
                                                <img :src="get_imgurl(article.author_avatar)" alt="" style="width:100%;height:100%;border-radius:50%;">
                                            </div>
                                            <div class="float-left ml-2 pt-1" style="font-weight:500;">
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
                    </div>
                </div>
            </div>
            <div class="c_r float-right">
                <div class="outer_box">
                    <div class="inner_box" style="width:106%;">
                        <div class="content_box">
                            <div class="calendar_box">
                                <Calendar v-on:choseDay="clickDay"></Calendar>
                            </div>
                            <div class="hot_articles">
                                <h5 style="border-bottom:1px solid #888;padding-bottom:10px">
                                    <span class="glyphicon glyphicon-fire" style="color:red;"></span>
                                    <span style="font-weight: bold;">本月热门推荐</span>
                                </h5>
                                <ul class="list-unstyled">
                                    <li v-for="(hot_art, hot_i) of hot_articles" :key="hot_i" style="font-size:14px;color:#000;" @click="to_article(hot_art.id,hot_art.author_id)">
                                        <p class="mb-0 cursor_pointer text_red_hover">
                                            <span style="font-weight:500">{{hot_i+1}}</span>
                                            <span>{{hot_art.title}}</span>
                                        </p>
                                        <div style="color:#888;font-size:14px;margin-top:-4px;">
                                            <span class="glyphicon glyphicon-eye-open"></span>
                                            <span> {{hot_art.watch_count}}</span>
                                        </div>
                                    </li>
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
import Calendar from './calendar'
import {getIndexArticles,getDayArticles,getTagArticles,getTitleArticles,getNicknameArticles} from '../assets/js/apis/forum'

export default {
    name: "Forum",
    data(){
        return{
            search_text:"",
            all_articles: [],
            hot_articles: [],
            display_articles: [],
            search_condition: "",
            condition_text: "",
            condition_articles_count: null,
        }
    },
    methods:{
        clickDay(date){
            var date_arr = date.split('/');
            this.search_condition = "日期";
            this.condition_text = date;
            getDayArticles(date_arr[0],date_arr[1],date_arr[2]).then(result=>{
                if (result.code==200){
                    this.display_articles = result.data;
                    this.condition_articles_count = result.data.length;
                }else{
                    alert(result.error)
                }
            });
            this.search_text = "";
        },
        get_imgurl(url){
            if (!url){
                return "../../static/img/index_bg.jpg"
            }else{
                return this.axios.defaults.baseURL+"static/"+url
            }
        },
        to_article(article_id,author_id){
            var {href} = this.$router.resolve({path: '/article', query:{author_id:author_id, article_id:article_id}});
            window.open(href, '_blank');
        },
        get_tag_articles(){
            this.search_condition = "标签";
            this.condition_text = this.search_text;
            getTagArticles(this.search_text).then(result=>{
                if (result.code==200){
                    this.display_articles = result.data;
                    this.condition_articles_count = result.data.length;
                }else{
                    alert(result.error)
                }
            });
            this.search_text = ""; 
        },
        get_author_articles(){
            this.search_condition = "作者";
            this.condition_text = this.search_text;
            getNicknameArticles(this.search_text).then(result=>{
                if (result.code==200){
                    this.display_articles = result.data;
                    this.condition_articles_count = result.data.length;
                }else{
                    alert(result.error)
                }
            });
            this.search_text = "";
        },
        get_title_articles(){
            this.search_condition = "标题";
            this.condition_text = this.search_text;
            getTitleArticles(this.search_text).then(result=>{
                if (result.code==200){
                    this.display_articles = result.data;
                    this.condition_articles_count = result.data.length;
                }else{
                    alert(result.error)
                }
            });
            this.search_text = "";
        },
        remove_tag(){
            this.search_condition = "";
            this.display_articles = this.all_articles;
        }
    },
    components: {
        Calendar,
    },
    created(){
        getIndexArticles().then(result=>{
            this.all_articles = result.data;
            this.display_articles = this.all_articles;
            this.hot_articles = result.hot_topics;
        })
    }
}
</script>
<style scoped>
#forum{
    width: 100%;
    height: 100%;
}
#forum>.container{
    height:100%;
    background-color: rgba(115, 176, 214, 0.4);
}
.c_l{
    width:800px;
    height: 100%;
    /* border: 1px solid red; */
}
.c_r{
    margin-right:10px;
    width: 300px;
    height: 100%;
    /* border: 1px solid blue; */
}
.search{
    position: absolute;
    width: 60%;
    padding: 5px;
    left: 10px;
    background: #fff;
    border: 1px solid #888;
    border-radius: 6px;
    font-size: 14px;
    text-align: center;
}
.search>#search{
    text-indent: 10px;
    height: 1.8rem;
    line-height: 1.8rem;
    width:100%;
    border: none;
    outline: none;
}
.search>.search_ico{
    position: absolute;
    width: 50px;
    height: 100%;
    right: 0;
    top:0;
    padding-top:3px;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    font-size: 1.5rem;
    background: #e1e2e9;
    color: #b2b2b2;
    /* cursor: pointer; */
}
.search>.search_ico:hover{
    background: #ddd;
}
.search_select{
    position: absolute;
    width: 70%;
    top: 57px;
    left: 10px;
    color: #000;
    background: #f0f0f0;
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
.hot_articles{
    margin: 10px auto;
    padding: 10px;
    background: #fff;
}
.topic_type{
    position: absolute;
    width: 250px;
    right:35px;
    font-size:14px;
    height: 2.5rem;
    line-height: 2.5rem;
    padding: 0 10px;
    text-align: left;
    background: #fff;
    border-radius: 5px;
}
.display_count{
    margin-top: 10px;
    height: 20px;
    line-height: 20px;
    padding: 0 5px;
    background: #3399ea;
    color: #fff;
    border-top-left-radius: 50%;
    border-top-right-radius: 50%;
    border-bottom-left-radius: 50%;
}
</style>