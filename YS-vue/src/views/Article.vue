<template>
    <div id="article">
        <div class="at_container clearfix">
            <main class="article_main">
                <div class="content_outer_box">
                    <div class="content_inner_box">
                        <div class="content_box">
                            <div class="content_header my-2">
                                <div class="content_header_box">
                                    <h1 style="font-size:28px;font-weight:bold;" class="mt-3">{{article_title}}</h1>
                                    <div class="content_hearder_bar pb-3 pt-1 clearfix">
                                        <div class="ml-2 float-left">
                                            <span class="header_article_username to_conclusion" @click="to_personal_conclusion(author_id)">{{author_nickname}}</span>
                                        </div>
                                        <div class="float-right">
                                            <span class="glyphicon glyphicon-eye-open"></span>
                                            <span>{{article_watch_count}}</span>
                                        </div>
                                        <div class="float-right mr-4">
                                            <span class="glyphicon glyphicon-star-empty"></span>
                                            <span>{{article_collect_count}}</span>
                                        </div>
                                        <div class="float-right mr-4">
                                            <span class="glyphicon glyphicon-heart-empty"></span>
                                            <span>{{article_like_count}}</span>
                                        </div>
                                        <div class="float-right mr-4">
                                            <span>发布于{{article_created_time}}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div id="content_body" v-html="article_content">
                                <!-- {{article_content}} -->
                            </div>
                            <div class="message_box">
                                <div class="message_issue">
                                    <div class="message_issue_top row mx-0">
                                        <div class="col-1 p-3" style="height:70px;">
                                            <img :src="get_imgurl(user_avatar)" alt="avatar" class="user_avatar cursor_pointer_hover">
                                        </div>
                                        <div class="col-11">
                                            <textarea name="user_message_text" id="user_message_text" class="form-control mt-1" :placeholder="message_placeholder" v-model="user_message_text"></textarea>
                                        </div>
                                    </div>
                                    <div class="message_issue_bottom clearfix" v-show="message_issue_bottom_flag">
                                         <div class="publish_message_btn_box">
                                            <button class="publish_message_btn" id="publish_message" @click="publish_message">发表评论</button>
                                        </div>
                                        <div class="message_text_count">
                                            <span>{{'还能输入'+(200-user_message_text.length)+'/200个字符'}}</span>
                                        </div>
                                    </div>
                                </div>
                                <hr>
                                <div class="message_body_box">
                                    <ul class="list-unstyled">
                                        <li class="my-2" style="border-bottom: 1px dashed #ccc" v-for="(message,i) of article_messages" :key="i">
                                            <div class="message_area">
                                                <div class="mx-0 clearfix" style="height:40px;line-height:40px;">
                                                    <div class="px-0 float-left">
                                                        <div class="message_user_avatar cursor_pointer_hover">
                                                            <img :src="get_imgurl(message.u_avatar)" alt="message_user_avatar" style="width:100%;height:100%;border-radius:50%;" @click="to_personal_conclusion(message.u_id)">
                                                        </div>    
                                                    </div>
                                                    <span class="float-left ml-1 px-0 cursor_pointer_hover bg_theme_hover" style="font-size:16px;font-weight:bold;margin-left:-20px;" @click="to_personal_conclusion(message.u_id)">{{message.user}}</span>
                                                    <span class="float-right cursor_pointer_hover bg_theme_hover" @click="open_close_reply($event,message.reply_count,message.m_id)" :data-distext="'查看回复('+message.reply_count+')'" v-show="message.reply_count">{{'查看回复('+message.reply_count+')'}}</span>
                                                    <span class="float-right mr-4 cursor_pointer_hover bg_theme_hover" @click="reply_click(message)">回复</span>
                                                    <span class="float-right mr-4 px-0">{{message.created_time}}</span>
                                                    <!-- <span class="col-1 glyphicon glyphicon-thumbs-up cursor_pointer_hover bg_theme_hover" style="margin-top:11px;">{{message.like_count}}</span> -->
                                                </div>
                                                <div class="py-1 pl-3">
                                                    <p>{{message.content}}</p>
                                                </div>
                                            </div>
                                            <ul class="list-unstyled" style="margin-left:30px;border-left: 3px solid #888;display:none" :id="message.m_id">
                                                <li class="mb-2" v-for="(reply, j) of message.replys" :key="j">
                                                    <div class="reply_area">
                                                        <div class="mx-0 clearfix" style="height:30px;line-height:30px;">
                                                            <div class="px-0 float-left">
                                                                <div class="reply_user_avatar cursor_pointer_hover">
                                                                    <img :src="get_imgurl(reply.u_avatar)" alt="reply_user_avatar" style="width:100%;height:100%;border-radius:50%;" @click="to_personal_conclusion(reply.u_id)">
                                                                </div>
                                                            </div>
                                                            <span class="float-left ml-1 px-0 cursor_pointer_hover bg_theme_hover" style="margin-left:-20px;" @click="to_personal_conclusion(reply.u_id)">{{reply.user}}</span>
                                                            <span class="float-right cursor_pointer_hover bg_theme_hover" @click="sub_reply_click(message, reply)">回复</span>
                                                            <span class="float-right mr-4 px-0 offset-4">{{reply.created_time}}</span>
                                                            <!-- <span class="col-1 glyphicon glyphicon-thumbs-up cursor_pointer_hover bg_theme_hover" style="margin-top:6px;">{{reply.like_count}}</span> -->
                                                        </div>
                                                    </div>
                                                    <div class="py-1 pl-3">{{reply.content}}</div>
                                                    <div class="ml-5 px-3 py-2" style="background: #ccc;" v-text="'@'+reply.parent_reply.user+': '+reply.parent_reply.content" v-show="reply.parent_reply.r_id"></div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
            <div class="tool_box">
                <ul class="list-unstyled">
                    <li class="like_li" :class="is_liked_li()" @click="like_or_cancel">
                        <p style="margin-bottom: -2px">点赞</p>
                        <span class="glyphicon glyphicon-heart-empty"></span>
                        <p class="my-0">{{article_like_count}}</p>
                    </li>
                    <li class="collection_li" :class="is_collected_li()" @click="collect_or_cancel">
                        <p style="margin-bottom: -2px">收藏</p>
                        <span class="glyphicon glyphicon-star-empty"></span>
                        <p class="my-0">{{article_collect_count}}</p>
                    </li>
                    <li class="message_li" @click="jump_to_message">
                        <p style="margin-bottom: -2px">评论</p>
                        <span class="glyphicon glyphicon-comment"></span>
                        <p class="my-0">{{message_count}}</p>
                    </li>
                    <li class="previon_li" v-show="prev_shield()" @click="to_article(previous_id)">
                        <span class="glyphicon glyphicon-menu-left mt-3"></span>
                        <p class="my-0">上一篇</p>
                    </li>
                    <li class="next_li" v-show="next_shield()" @click="to_article(next_id)">
                        <span class="glyphicon glyphicon-menu-right mt-3"></span>
                        <p class="my-0">下一篇</p>
                    </li>
                </ul>
            </div>
            <aside class="article_aside">
                <div class="outer_box">
                    <div class="inner_box">
                        <div class="box">
                            <div class="author_info p-2 pt-4 bg-white box_shadow">
                                <div class="row mx-0 " style="height:40px;line-height:40px;">
                                    <img :src="get_imgurl(author_avatar)" alt="author_avatar" style="width:100%;height:100%;border-radius:50%;" class="col-3 cursor_pointer_hover" @click="to_personal_conclusion(author_id)">                    
                                    <span class="col-9 author_name to_conclusion" @click="to_personal_conclusion(author_id)">{{author_nickname}}</span>   
                                </div>
                                <hr>
                                <div class="row mx-0">
                                    <span class="col-6 to_conclusion" style="font-size:14px" @click="to_personal_conclusion(author_id)">ta的个人总结页></span>
                                    <button class="col-4 offset-2 attention_btn" :class="attention_btn_bg()" @click="attention_or_cancel">{{attention_btn_text()}}</button>    
                                </div>                                  
                            </div>
                            <div class="hot_article mt-4 p-2 pt-4 bg-white box_shadow" style="font-size:14px">
                                <h5 style="font-weight:bold;">热门总结</h5>
                                <div v-for="(topic, index) of hot_conclusion" :key="index">
                                    <p style="word-break: break-all;" class="mb-0 cursor_pointer_hover bg_theme_hover" @click="to_article(topic.id)">{{topic.title}}</p>
                                    <span class="glyphicon glyphicon-eye-open"></span> {{topic.watch_count}}
                                    <hr class="my-1">
                                </div> 
                            </div>
                            <div class="beian_info mt-2 p-2 bg-white box_shadow text-center">
                                <a href="http://www.beian.miit.gov.cn" target="_blank" class="text-dark text-decoration-none" style="font-size:14px;color:#666;">鄂ICP备200002048</a>
                            </div>
                        </div>
                    </div>
                </div>
                
            </aside>
        </div>
    </div>
</template>
<script>
import {getArticle,getUserInfo,getAuthorArticles,getFans,getMessages,getCollections,getLikes,createFollow,createMessage,createReply,createCollection,createLike,deleteLike,deleteCollection,createWatch,deleteFollow} from "../assets/js/apis/article.js"



export default {
    name: 'Article',
    data(){
        return {
            user_message_text: "",
            message_issue_bottom_flag: false,
            article_id: null,
            article_title: "",
            article_content: "",
            article_created_time: "",
            article_watch_count: 0,
            article_like_count: 0,
            article_collect_count: 0,
            message_count: 0,
            author_id: null,
            author_nickname: "",
            hot_conclusion: [],
            is_liked: false,
            is_collected: false,
            is_attention: false,
            user_avatar: "",
            author_avatar: "",
            previous_id: null,
            next_id: null,
            article_messages:[],
            message_placeholder: "想说点什么",
            message_level: "message",
            message_object_id: null,
            reply_object_id: null,
        }
    },
    methods: {
        jump_to_message(){
            var message = document.getElementById("user_message_text");
            message.focus();
        },
        is_liked_li(){
            if (this.is_liked){
                return "is_liked_li"
            }
        },
        is_collected_li(){
            if (this.is_collected){
                return "is_collected_li"
            }
        },
        like_or_cancel(){
            if (this.is_liked){
                deleteLike(this.article_id).then(result=>{
                    if (result.code==200){
                        this.is_liked=!this.is_liked;
                        this.article_like_count--;
                    }else if(result.code==10202){
                        alert('会话已过期,请重新登陆');
                        localStorage.removeItem('ytoken');
                        localStorage.removeItem('user_id');
                        this.$router.push({name:'Index'})
                    }else{
                        alert(result.error)
                    }
                })
            }else{
                createLike({t_id:this.article_id}).then(result=>{
                    if (result.code==200){
                        this.is_liked=!this.is_liked;
                        this.article_like_count++;
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
        collect_or_cancel(){
            if (this.is_collected){
                deleteCollection(this.article_id).then(result=>{
                    if (result.code==200){
                        this.is_collected=!this.is_collected;
                        this.article_collect_count--;
                    }else if(result.code==10202){
                        alert('会话已过期,请重新登陆');
                        localStorage.removeItem('ytoken');
                        localStorage.removeItem('user_id');
                        this.$router.push({name:'Index'})
                    }else{
                        alert(result.error)
                    }
                })
            }else{
                createCollection({t_id:this.article_id}).then(result=>{
                    if (result.code==200){
                        this.is_collected=!this.is_collected;
                        this.article_collect_count++;
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
        open_close_reply(e,reply_count,reply_dis_id){
            if (e.target.textContent == '收起回复'){
                var replys = document.getElementById(String(reply_dis_id));
                replys.style.display = 'none';
                e.target.textContent = e.target.dataset.distext;
            }else{
                if (reply_count != 0){
                    var replys = document.getElementById(String(reply_dis_id));
                    replys.style.display = "block";
                    e.target.textContent = '收起回复'
                }
            }
        },
        get_imgurl(url){
            if (!url){
                return "../../static/img/index_bg.jpg"
            }else{
                return this.axios.defaults.baseURL+"static/"+url
            }
        },
        get_messages(){
            this.user_message_text = "";
            getMessages(this.article_id).then(result=>{
                if (result.code==200){
                    this.article_messages=result.data.sort((a,b)=>{
                        return b.reply_count - a.reply_count
                    })
                }else{
                    alert(result.error)
                }
            });
        },
        reply_click(message){
            this.message_object_id = message.m_id;
            this.message_level = "reply";
            this.message_placeholder = "@"+message.user+": ";
            this.jump_to_message();
        },
        sub_reply_click(message,reply){
            this.message_object_id = message.m_id;
            this.reply_object_id = reply.r_id;
            this.message_level = "subreply";
            this.message_placeholder = "@"+reply.user+": "
            this.jump_to_message();
        },
        publish_message(){
            switch (this.message_level){
                case "message":
                    var data = {t_id:this.article_id, content: this.user_message_text};
                    createMessage(data).then(result=>{
                        if (result.code==200){
                            this.message_count++;
                            this.get_messages();
                        }else if(result.code==10202){
                            alert('会话已过期,请重新登陆');
                            localStorage.removeItem('ytoken');
                            localStorage.removeItem('user_id');
                            this.$router.push({name:'Index'})
                        }else{
                            alert(result.error)
                        }
                    });
                    break;
                case "reply":
                    var data = {message_id:this.message_object_id,content:this.user_message_text,is_second_reply:false};
                    createReply(data).then(result=>{
                        if (result.code==200){
                            this.message_count++;
                            this.get_messages();
                        }else if(result.code==10202){
                            alert('会话已过期,请重新登陆');
                            localStorage.removeItem('ytoken');
                            localStorage.removeItem('user_id');
                            this.$router.push({name:'Index'})
                        }else{
                            alert(result.error)
                        }
                    })
                    break;
                case "subreply":
                    var data = {message_id:this.message_object_id,content:this.user_message_text,is_second_reply:true,parent_reply_id:this.reply_object_id};
                    createReply(data).then(result=>{
                        if (result.code==200){
                            this.message_count++;
                            this.get_messages()
                        }else if(result.code==10202){
                            alert('会话已过期,请重新登陆');
                            localStorage.removeItem('ytoken');
                            localStorage.removeItem('user_id');
                            this.$router.push({name:'Index'})
                        }else{
                            alert(result.error)
                        }
                    })
                    break;
            };
            this.message_placeholder = "想说点什么";
            this.message_level = "message";
        },
        prev_shield(){
            return this.previous_id?true:false
        },
        next_shield(){
            return this.next_id?true:false
        },
        to_article(article_id){
            this.$router.push({path:'/article',query:{article_id:article_id,author_id:this.author_id}})
        },
        attention_btn_bg(){
            if (this.is_attention){
                return "bg_attention_red"
            }
        },
        attention_btn_text(){
            if (this.is_attention){
                return "已关注"
            }else{
                return "关注"
            }
        },
        attention_or_cancel(){
            if (this.is_attention){
                deleteFollow(this.author_id).then(result=>{
                    if (result.code==200){
                        this.is_attention=!this.is_attention
                    }else if(result.code==10202){
                        alert('会话已过期,请重新登陆');
                        localStorage.removeItem('ytoken');
                        localStorage.removeItem('user_id');
                        this.$router.push({name:'Index'})
                    }else{
                        alert(result.error)
                    }
                })
            }else{
                createFollow(this.author_id).then(result=>{
                    if (result.code==200){
                        this.is_attention=!this.is_attention
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
        to_personal_conclusion(personal_id){
            this.$router.push({name:'Personal', query:{personal_id}})
        }       
    },
    watch:{
        user_message_text(){
            if (this.user_message_text.length==0){
                this.message_issue_bottom_flag=false;
            }else if(this.user_message_text.length>0){
                this.message_issue_bottom_flag = true;
            };
            if(this.user_message_text.length>200){
                this.user_message_text = this.user_message_text.slice(0,200)
            }
        },
        $route(to, from){
            this.$router.go(0);
        }

    },
    created(){
        var url_query = this.$route.query;
        var user_id = localStorage.getItem("user_id");
        this.article_id = url_query.article_id;
        this.author_id = url_query.author_id;
        getArticle(this.article_id).then(result=>{
            if (result.code==200){
                this.article_title = result.data.title;
                this.author_nickname = result.data.author_name;
                this.article_content = result.data.content;
                this.article_created_time = result.data.created_time;
                this.article_watch_count = result.data.watch_count;
                this.article_like_count = result.data.like_count;
                this.article_collect_count = result.data.collect_count;
                this.previous_id = result.data.prev_id;
                this.next_id = result.data.next_id;
                this.message_count = result.data.message_count;
            }else if(result.code==10202){
                alert('会话已过期,请重新登陆');
                localStorage.removeItem('ytoken');
                localStorage.removeItem('user_id');
                this.$router.push({name:'Index'})
            }else{
                alert(result.error)
            }
        });
        getLikes(this.article_id).then(result=>{
            if (result.code==200){
                if(result.data.indexOf(parseInt(user_id))!=-1){
                    this.is_liked = true
                }
            }else{
                alert(result.error)
            }
        });
        getCollections(user_id).then(result=>{
            if (result.code==200){
                if (result.topic_ids.indexOf(parseInt(this.article_id))!=-1){
                    this.is_collected = true;
                }
            }else{
                alert(result.error)
            }
            
        });
        this.get_messages();
        getAuthorArticles(this.author_id).then(result=>{
            if (result.code==200){
                this.hot_conclusion = result.data.sort((a,b)=>{
                    return b.watch_count-a.watch_count
                }).slice(0,10);
            }else if(result.code==10202){
                alert('会话已过期,请重新登陆');
                localStorage.removeItem('ytoken');
                localStorage.removeItem('user_id');
                this.$router.push({name:'Index'})
            }else{
                alert(result.error)
            }
        });
        getUserInfo(user_id).then(result=>{
            if (result.code==200){
                this.user_avatar = result.data.avatar
            }else{
                alert(result.error)
            }
        });
        getUserInfo(this.author_id).then(result=>{
            if (result.code==200){
                this.author_avatar = result.data.avatar
            }else{
                alert(result.error)
            }
        });
        getFans(this.author_id).then(result=>{

            if (result.code==200){
                if (result.data.indexOf(parseInt(user_id))!=-1){
                    this.is_attention = true
                }
            }else{
                alert(result.code)
            }
        });
        setTimeout(()=>{
            createWatch({t_id:this.article_id}).then(result=>{
                if (result.code==200){
                    this.article_watch_count++;
                }else if(result.code==10202){
                    alert('会话已过期,请重新登陆');
                    localStorage.removeItem('ytoken');
                    localStorage.removeItem('user_id');
                    this.$router.push({name:'Index'})
                }else{
                    alert(result.error)
                }
            })
        },30000)
    }
}
</script>
<style scoped>
#article{
    padding-top: 40px;
    width: 100%;
    height: 100%;
    background-image: linear-gradient(to bottom,  #72afd5, #b0d7ee);
}
#article>.at_container{
    width: 1250px !important;
    height: 100%;
    padding-top: 10px;
    margin: 0 auto !important;
    /* border: 1px solid red; */
}
.article_main{
    float: left;
    width: 880px;
    height: 100%;
    background: #fff;
    padding: 0 24px;
    box-shadow: 0 0 12px 0;
}
.tool_box{
    /* position: fixed; */
    float: left;
    width: 50px;
    margin-left:1px;
    background: #fff;
    box-shadow: 0 0 4px 0;
    font-size: 13px;
}
.tool_box li{
    height: 60px;
    /* line-height: 50px; */
    text-align: center;
    color: #444;
    border-bottom: 1px solid #999;
}
.tool_box li:hover{
    cursor: pointer;
    color: red;
}
.article_aside{
    float: right;
    width: 300px;
    height: 100%;
    /* background: #fff; */
    /* box-shadow: 0 0 4px 0; */
}
.content_outer_box{
    position: relative;
    width: 832px;
    height: 100%;
    overflow: hidden;
}
.content_inner_box{
    position: absolute;
    height: 100%;
    left: 0;
    overflow-x: hidden;
    overflow-y: scroll;
}
.content_box{
    width: 832px;
    height: 100%;
}
.content_hearder_bar{
    border-bottom: 1px solid #666;
    color: #666;
}
.message_box{
    margin-top: 30px;
    margin-bottom: 30px;
    /* border-top: 1px solid red; */
}
.user_avatar{
    border-radius: 50%;
    width: 100%;
    height: 100%;
    box-shadow: 0 0 3px 0 #fff;
}
.message_text_count{
    float: right;
    margin-top: 4px;
    margin-right: 10px;
    color: #666;
}
.publish_message_btn_box{
    float: right;
    margin-right: 15px;
}
.publish_message_btn{
    color: #555;
    padding: 3px 6px;
    border-radius: 2px;
    background: #fff;
    border: 1px solid red;
}
.publish_message_btn:hover{
    background: red;
    color: #fff;
}
.to_conclusion{
    color: #3399ea;
}
.to_conclusion:hover{
    cursor: pointer;
}
.attention_btn{
    background: #fff;
    border: 1px solid #444;
    border-radius: 2px;
}
.attention_btn:hover{
    background: red;
    color: #fff;
    border-color: red;
}
.box_shadow{
    box-shadow: 0 0 4px 0;
}
.outer_box{
    position: relative;
    width: 300px;
    height: 100%;
    overflow: hidden;
}
.inner_box{
    position: absolute;
    width: 320px;
    height: 100%;
    left: 0;
    overflow-x: hidden;
    overflow-y: scroll;
}
.box{
    width: 300px;
    height: 100%;
}
.beian_info>a:hover{
    color: #39c3cf !important;
}
.is_liked_li{
    color: red !important;
}
.is_collected_li{
    color: red !important;
}
.message_body_box{
    /* border: 1px solid red; */
    color: #666;
    font-size: 14px;
}
.message_user_avatar{
    width: 30px;
    height: 30px;
    margin-left: 10px;
}
.reply_user_avatar{
    width: 25px;
    height: 25px;
    margin-left: 10px;
}
.cursor_pointer_hover:hover{
    cursor:pointer;
}
.bg_theme_hover:hover{
    color: #39c3cf;
}
.color_red{
    color: red !important;
}
.previon_li{
    position: relative;
}
.next_li{
    position: relative;
}
.bg_attention_red{
    background:red;
    color: #fff;
    border-color: red;
}
</style>