<template>
    <div id="md">
        <div class="inner_issue" :style="{top:inner_issue_top}">
            <div class="inner_body">
                <h5 style="font-weight:600;margin-bottom: 1rem;">总结发布</h5>
                <hr>
                <div class="form-group row mx-0 text-center mb-3">
                    <p class="col-4 mt-2 mb-0">总结标签</p>
                    <input type="text" class="form-control col-8" placeholder="eg: python、mysql" v-model="label">
                </div>
                <div class="row mx-0 text-center" style="line-height:40px">
                    <p class="col-4 mb-0">总结形式</p>
                    <input type="radio" name="article_limit" value="public" class="col-2 mt-3 " checked v-model="limit">公开
                    <input type="radio" name="article_limit" value="private" class="col-2 mt-3 " v-model="limit">私有
                </div>
                <div class="clearfix mt-4">
                    <span style="margin-left:100px" class="close_inner_issue" @click="close_inner_issue">取消</span>
                    <button class="issue" @click="issue_article">发布</button>
                </div>
            </div>
        </div>
        <div class="md_header row mx-0">
            <div class="col-10 h-100 from-group">
                <input type="text" class="form-control" id="title" placeholder="请输入标题" v-model="title_text">
            </div>
            <div class="col-1 h-100 pt-2">
                <span >{{title_length+"/"+title_max_length}}</span>
            </div>
            <div class="col-1 h-100" >
                <button class="btn_issue" @click="open_inner_issue">发布</button>
            </div>
        </div>
        <div class="md_body">
            <mavon-editor v-model="content" ref="md" @change="change" @imgAdd="img_add" style="height:100%"/>
        </div>
    </div>
</template>
<script>
import { mavonEditor } from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import {createArticle, createImage} from "../assets/js/apis/md.js"

export default {
    name: "Md",
    data() {
        return {
            content: "",
            html: "",
            title_length: 0,
            title_max_length: 100,
            title_text: "",
            inner_issue_top: "-100%",
            label: "",
            limit: "public",
        }
    },
    methods:{
        change(value, render){
            this.html = render
        },
        img_add(pos, $file){
            let formdata = new FormData();
            formdata.append('topic_image', $file);
            createImage(formdata).then(result=>{
                if (result.code==200){
                    this.$refs.md.$img2Url(pos,this.axios.defaults.baseURL+"static/"+result.img_url)
                }else{
                    alert(result.error)
                }
            })
        },
        close_inner_issue(){
            this.inner_issue_top = "-100%";
        },
        open_inner_issue(){
            this.inner_issue_top = "0"
        },
        issue_article(){
            var re1 = new RegExp("<.+?>","g");
            var re2 = new RegExp("\n", "g")
            var data = {
                type: this.label,
                title: this.title_text,
                content: this.html,
                introduce: this.html.replace(re1,"").replace(re2, " ").slice(0,30),
                limit: this.limit
            };
            createArticle(data).then(result=>{
                if (result.code==200){
                    this.$router.push({path:'/article', query:{article_id:result.topic_id,author_id:result.author_id}});
                    // this.close_inner_issue();
                    // alert(result.topic_id);
                }else{
                    alert(result.code, result.error);
                }
            })
        }
    },
    components:{
        mavonEditor
    },
    watch:{
        title_text(){
            if (this.title_text.length <= 100){
                this.title_length = this.title_text.length
            }else{
                this.title_text = this.title_text.slice(0,100);
            }
        }
    }
}
</script>
<style scoped>
#md{
    position: absolute;
    width: 100%;
    height: 100%;
}
.md_header{
    width: 100%;
    height: 6%;
    /* border: 1px solid red; */
}
.md_header>div+div{
    margin-left: -1%;
}
.md_body{
    height: 94%;
}
.btn_issue{
    width: 90px;
    height: 38px;
    /* margin-top: 3%; */
    border: 1px solid red;
    border-radius: 3px;
    background: #fff;
}
.btn_issue:hover{
    background:red;
    color: #fff;
}
.issue{
    width:30%;
    padding: 5px 0;
    float: right;
    border: 1px solid #666;
    border-radius: 2px;
    background: #fff;
    transition: all 0.25s;
}
.issue:hover{
    background: red;
    border: 1px solid red;
    color: #fff;
}
.close_inner_issue{
    padding: 10px;
}
.close_inner_issue:hover{
    cursor: pointer;
    color: #17a2b8
}
.inner_issue{
    position: fixed;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.2);
    z-index: 9999;
    transition: all 0.3s;
}
.inner_issue>.inner_body{
    width: 30%;
    height: 40%;
    margin: 10% auto;
    padding: 2% 3%;
    background-color: #fff;
    box-shadow: 0 0 10px 0 #fff;
    border-radius: 4px;
}
</style>