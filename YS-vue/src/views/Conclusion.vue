<template>
    <div id="conclusion">
        <my-header></my-header>
        <div class="conclusion_header">
            <div class="row">
                <p class="col-2 h4">总结管理</p>
                <div class="col-10">
                    <ul class="row list-unstyled" style="font-size:14px;" @click="select_nav">
                        <li class="col-1 px-0 text-center cursor_hover bg_dark_hover" :class="nav_select_bg(`forum`)">论坛页</li>
                        <li class="col-1 px-0 text-center cursor_hover bg_dark_hover" :class="nav_select_bg(`personal`)">总结页</li>
                        <li class="col-1 px-0 text-center cursor_hover bg_dark_hover">写总结</li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="conclusion_body">
            <router-view/>
        </div>
    </div>
</template>
<script>
import '../assets/css/myheader.css'
// import '../assets/css/myfooter.css'

export default {
    name: "Conclusion",
    data(){
        return {
            nav_select: "personal"
        }
    },
    methods:{
        nav_select_bg(select){
            if (select==this.nav_select){
                return 'bg_dark'
            }
        },
        select_nav(e){
            switch (e.target.textContent){
                case "论坛页":
                    this.nav_select="forum";
                    break;
                case "总结页":
                    this.nav_select="personal";
                    break
            }
        }
    }
}
</script>
<style scoped>
.cursor_hover:hover{
    cursor: pointer;
}
.bg_dark_hover:hover{
    background: rgba(0, 0, 0, 0.4);
}
.bg_dark{
    background: rgba(0, 0, 0, 0.2);
}
#conclusion{
    width: 100%;
    height: 100%;
    /* background: #444; */
}
#conclusion>.conclusion_header{
    position: fixed;
    height: 40px;
    width: 60%;
    margin-left:80px;
    top:0;
    z-index: 100;
    line-height: 40px;
    color: #f5f5f5;
    /* background: #; */
}
#conclusion>.conclusion_body{
    width: 100%;
    height: 100%;
    padding-top: 40px;
    /* border: 1px solid red; */
}
</style>