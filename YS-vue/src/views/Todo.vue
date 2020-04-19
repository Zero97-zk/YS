<template>
    <div id="todo">
        <my-header></my-header>
        <div id="update_todo" :style="{top:update_todo_top}">
            <div class="close_add_todo" @click="closeUpdate"><span>&times;</span></div>
            <div class="update_content text-center">
                <div class="form-group pt-1">
                    <label for="update_level">待办等级</label>
                    <select class="form-control" id="update_level">
                        <option value="a">A:特急</option>
                        <option value="b">B:加急</option>
                        <option value="c">C:常规</option>
                        <option value="d">D:稍缓</option>
                    </select>
                </div>
                    <div class="form-group pt-1">
                    <label for="update_state">状态</label>
                    <select class="form-control" id="update_state">
                        <option value="todo">待办</option>
                        <option value="completed">已完成</option>
                    </select>
                </div>
                <hr class="my-1">
                <div class="form-group">
                    <label for="update_content">待办内容</label>
                    <textarea class="form-control" rows="3" id="update_content"></textarea>
                </div>
                <div style="margin-top:18px;">
                    <button class="btn btn-default btn_update mr-2" @click="updateTodo">修改</button>
                    <button class="btn btn-default btn_update ml-2" @click="deleteTodo">删除</button>
                </div>
            </div>
        </div>
        <div id="add_todo" :style="{top:add_todo_top}">
            <div class="close_add_todo" @click="closeAdd"><span>&times;</span></div>
            <div class="add_content text-center">
                <div class="form-group pt-1">
                    <label for="add_level">待办等级</label>
                    <select class="form-control" id="add_level">
                        <option value="a">A:非常重要</option>
                        <option value="b">B:重要</option>
                        <option value="c">C:一般</option>
                        <option value="d">D:可稍缓</option>
                    </select>
                </div>
                <div class="form-group pt-1">
                    <label for="add_state">状态</label>
                    <select class="form-control" id="add_state">
                        <option value="todo">待办</option>
                        <option value="completed">已完成</option>
                    </select>
                </div>
                <hr class="my-1">
                <div class="form-group">
                    <label for="add_content">待办内容</label>
                    <textarea class="form-control" rows="3" id="add_content"></textarea>
                </div>
                <div style="margin-top:18px;">
                    <button class="btn btn-default btn_add" @click="addTodo">添加</button>
                </div>
            </div>
        </div>
        <div id="todo_header">
            <div class="row">
                <p class="col-2 h4">行动日志</p>
                <div class="col-10">
                    <ul class="row list-unstyled" @click="update_todo_type">
                        <li class="first_menu" :class="nav_select_bg(`day`)">日待办</li>
                        <li class="first_menu" :class="nav_select_bg(`week`)">周待办</li>
                        <li class="first_menu" :class="nav_select_bg(`month`)">月待办</li>
                        <li class="first_menu" :class="nav_select_bg('year')">年待办</li>
                    </ul>
                </div>
            </div>
        </div>
        <div id="todo_body" class="clearfix">
            <div class="body_left">
                <div class="outer_box">
                    <div class="inner_box">
                        <div class="content_box">
                            <div class="body_top row mx-0 pl-3">
                                <div class="not_completed col-3 ">
                                    <label for="radio_input" class="mb-0 radio_label">未完成<span class="todo_count">{{get_todo_count()}}</span></label>
                                    <input id="radio_input" type="checkbox" class="radio_input" v-model="show_only_todo">
                                </div>
                            </div>
                            <hr>
                            <div class="todo_action row mx-0" >
                                <div class="card col-3" @click="showAdd">
                                    <div class="card-header"></div>
                                    <div class="card-body text-center add_todo">
                                        <span class="glyphicon glyphicon-plus"></span>
                                    </div>
                                    <div class="card-footer"></div>
                                </div>
                                <div class="card col-3" v-for="(todo, i) of display_todo" :key="i" :class="[addClassState(todo.state)]" @click="showUpdate(todo)" v-show="show_todo(todo.state)">
                                    <div class="card-header text-center pt-0 pb-0">
                                        <h5>{{todo.level | levelOut}}</h5>
                                    </div>
                                    <div class="card-body add_todo pt-1 pl-1 text-center">
                                        <p>{{todo.content}}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="body_right">
                <div class="my_calendar calendar_day" v-show="todo_type=='day'">
                    <Calendar v-on:choseDay="clickDay"></Calendar>
                </div>
                <div class="my_calendar calendar_week" v-show="todo_type=='week'">
                    <div class="calendar_header row mx-0">
                        <div class="col-2 cursor_pointer" @click="update_year(-1)">
                            <div class="calendar_header_left"></div>
                        </div>
                        <div class="col-8">
                            <span class="week_year calendar_header_middle">{{chose_year}}</span>
                        </div>
                        <div class="col-2 cursor_pointer" @click="update_year(1)">
                            <div class="calendar_header_right"></div>
                        </div>
                    </div>
                    <div class="calendar_body mx-0 clearfix">
                        <div v-for="i of 53" :key="i" class="week_body calendar_pointer cursor_pointer" :class="get_week_bg(i)" @click="update_chose_week(i)">{{i}}</div>
                    </div>
                </div>
                <div class="my_calendar calendar_month" v-show="todo_type=='month'">
                    <div class="calendar_header row mx-0">
                        <div class="col-2 cursor_pointer" @click="update_year(-1)">
                            <div class="calendar_header_left"></div>
                        </div>
                        <div class="col-8">
                            <span class="month_year calendar_header_middle">{{chose_year}}</span>
                        </div>
                        <div class="col-2 cursor_pointer" @click="update_year(1)">
                            <div class="calendar_header_right"></div>
                        </div>
                    </div>
                    <div class="calendar_body mx-0 clearfix">
                        <div v-for="i of 12" :key="i" class="month_body calendar_pointer cursor_pointer" :class="get_month_bg(i)" @click="update_chose_month(i)">{{i}}</div>
                    </div>
                </div>
                <div class="my_calendar calendar_year" v-show="todo_type=='year'">
                    <div class="calendar_header row mx-0">
                        <div class="col-2 cursor_pointer" @click="update_year(-1)">
                            <div class="calendar_header_left"></div>
                        </div>
                        <div class="col-8">
                            <span class="month_year calendar_header_middle">{{chose_year}}</span>
                        </div>
                        <div class="col-2 cursor_pointer" @click="update_year(1)">
                            <div class="calendar_header_right"></div>
                        </div>
                    </div>
                </div>
                <div class="todo_conclusion" style="position:absolute;bottom:60px;right:0;width:100%;">
                    <div class="card">
                        <div class="card-header pt-0 pb-0">
                            <h5>总结</h5>
                        </div>
                        <div class="card-body">
                            完成度80%
                        </div>
                    </div>
                </div>
                <div class="beian mt-2 p-2 text-center" style="background: rgba(0, 0, 0, 0.5);position:absolute;bottom:10px;right:0;width:100%">
                    <a href="http://www.beian.miit.gov.cn" target="_blank" class="text-decoration-none" style="font-size:14px;color:#eee;">鄂ICP备200002048</a>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import Calendar from './calendar'
import {getIndexTodos, dayTodos, weekTodos, monthTodos, yearTodos} from '../assets/js/apis/todo.js'
import '../assets/css/myheader.css'
import '../assets/css/common.css'

export default {
    name: 'Todo',
    data() {
        return {
            day_todo:[],
            week_todo: [],
            month_todo: [],
            year_todo: [],
            display_todo: [],
            update_todo_top: "-100%",
            add_todo_top: "-100%",
            show_only_todo: false,
            todo_type: "day",
            chose_week: this.get_week(),
            chose_year: this.get_year(),
            chose_month: this.get_month(),
            chose_day: this.get_day(),
            display_year: this.get_year(),
        }
    },
    methods:{
        clickDay(data) {
            var date = data.split("/");
            var year = date[0];
            var month = date[1];
            var day = date[2];
            this.display_year = year;
            this.chose_day = Math.ceil(( new Date(year, parseInt(month)-1, parseInt(day)+1) - new Date(year))/(24*60*60*1000)); 
            this.get_day_todos();
        },
        addClassLevel(level){
            switch (level){
                case "a":return "bg_level_A";
                case "b":return "bg_level_B";
                case "c":return "bg_level_C";
                case "d":return "bg_level_D";
            }
        },
        addClassState(state){
            return state=="todo"?"no_completed":"completed"
        },
        showAdd(){
            this.add_todo_top="0";
        },
        closeAdd(){
            this.add_todo_top="-100%";
            document.getElementById("add_level").value = "a";
            document.getElementById("add_state").value = "todo";
            document.getElementById("add_content").value = "";
        },
        showUpdate(todo){
            let level = document.getElementById("update_level");
            let state = document.getElementById("update_state");
            let content = document.getElementById("update_content");
            let update_btn = document.getElementsByClassName("btn_update")
            level.value = todo.level;
            state.value = todo.state;
            content.value = todo.content;
            update_btn.todo = todo;
            this.update_todo_top="0";
        },
        closeUpdate(){
            this.update_todo_top="-100%";
        },
        addTodo(){
            var level = document.getElementById("add_level");
            var content = document.getElementById("add_content");
            var data = {
                level: level.value,
                content: content.value,
            }
            switch (this.todo_type){
                case "day":
                    data.year = this.display_year;
                    data.day = this.chose_day;
                    dayTodos("post",data.year, data.day, data).then(result=>{
                        if (result.code==200){
                            this.get_day_todos();
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
                case "week":
                    data.year = this.display_year;
                    data.week = this.chose_week;
                    weekTodos("post", data.year,data.week, data).then(result=>{
                        if (result.code==200){
                            this.get_week_todos();
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
                case "month":
                    data.year = this.display_year;
                    data.month = this.chose_month;
                    monthTodos("post", data.year, data.month, data).then(result=>{
                        if (result.code==200){
                            this.get_month_todos();
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
                case "year":
                    data.year = this.chose_year;
                    yearTodos("post", data.year, data).then(result=>{
                        if (result.code==200){
                            this.get_year_todos();
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
            };
            this.closeAdd()
        },
        updateTodo(){
            let update_btn = document.getElementsByClassName("btn_update");
            let level = document.getElementById("update_level");
            let state = document.getElementById("update_state");
            let content = document.getElementById("update_content");
            var data = {
                todo_id: update_btn.todo.todo_id,
                level: level.value,
                content: content.value,
                state: state.value,
            }
            switch (this.todo_type){
                case "day":
                    dayTodos("put", this.display_year, this.chose_day, data).then(result=>{
                        if (result.code==200){
                            this.get_day_todos();
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
                case "week":
                    weekTodos("put", this.display_year, this.chose_week, data).then(result=>{
                        if (result.code==200){
                            this.get_week_todos();
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
                case "month":
                    monthTodos("put", this.display_year, this.chose_month, data).then(result=>{
                        if (result.code==200){
                            this.get_month_todos().then();
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
                case "year":
                    yearTodos("put", this.display_year, data).then(result=>{
                        if (result.code==200){
                            this.get_year_todos();
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
            };
            this.closeUpdate()
        },
        deleteTodo(){
            let update_btn = document.getElementsByClassName("btn_update");
            switch (this.todo_type){
                case "day":
                    dayTodos("delete", update_btn.todo.todo_id).then(result=>{
                        if (result.code==200){
                            this.get_day_todos();
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
                case "week":
                    weekTodos("delete", update_btn.todo.todo_id).then(result=>{
                        if (result.code==200){
                            this.get_week_todos();
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
                case "month":
                    monthTodos("delete", update_btn.todo.todo_id).then(result=>{
                        if (result.code==200){
                            this.get_month_todos().then();
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
                case "year":
                    yearTodos("delete", update_btn.todo.todo_id).then(result=>{
                        if (result.code==200){
                            this.get_year_todos();
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
            };
            this.closeUpdate()
        },
        show_todo(state){
            return this.show_only_todo==false?true:state=="todo"?true:false;
        },
        update_todo_type(e){
            this.chose_week = this.get_week();
            this.chose_month = this.get_month();
            this.chose_year = this.get_year();
            switch(e.target.textContent){ 
                case "日待办":
                    this.todo_type="day";
                    this.display_todo = this.day_todo;
                    break
                case "周待办":
                    this.todo_type="week";
                    this.display_todo = this.week_todo;
                    break
                case "月待办":
                    this.todo_type="month";
                    this.display_todo = this.month_todo;
                    break
                case "年待办":
                    this.todo_type="year";
                    this.display_todo = this.year_todo;
                    break
            }
        },
        get_day_todos(){
            var year = this.display_year;
            var day = this.chose_day;
            dayTodos("get", year, day).then(result=>{
                if(result.code==200){
                    this.display_todo = result.data;
                    if (this.chose_day==this.get_day()&&year==this.get_year()){
                        this.day_todo=result.data;
                    };
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
        get_week_todos(){
            var year = this.display_year;
            var week = this.chose_week;
            weekTodos("get", year, week).then(result=>{
                if (result.code==200){
                    this.display_todo = result.data;
                    if (this.chose_week==this.get_week()&&year==this.get_year()){
                        this.week_todo=result.data
                    };
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
        get_month_todos(){
            var year = this.display_year;
            var month = this.chose_month;
            monthTodos("get", year, month).then(result=>{
                if (result.code==200){
                    this.display_todo = result.data;
                    if (this.chose_month==this.get_month()&&year==this.get_year()){
                        this.month_todo=result.data
                    };
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
        get_year_todos(){
            var year = this.chose_year;
            yearTodos("get", year).then(result=>{
                if (result.code==200){
                    this.display_todo = result.data;
                    if (year==this.get_year()){
                        this.year_todo=result.data
                    };
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
        get_day(){
            return Math.ceil(( new Date() - new Date(new Date().getFullYear().toString()))/(24*60*60*1000));
        },
        get_week(){
            var today = new Date();
            var first_day = new Date(today.getFullYear(), 0, 1);
            var day_of_week = first_day.getDay();
            if (day_of_week==1){
                return Math.ceil(((today.valueOf()-first_day.valueOf())/86400000)/7);
            }
            var spend_day = 1;
            if (day_of_week!=0){
                spend_day = 7- day_of_week+1;
            };
            first_day = new Date(today.getFullYear(), 0 ,1+spend_day);
            return Math.ceil(((today.valueOf()-first_day.valueOf())/86400000)/7)+1;
        },
        get_month(){
            var today = new Date();
            return today.getMonth()+1;
        },
        get_year(){
            var today = new Date();
            return today.getFullYear();
        },
        get_week_bg(current_week){
            var week = this.get_week();
            var year = this .get_year();
            if (year==this.chose_year && parseInt(current_week)==week){
               return "calendar_current"
            }else if(parseInt(current_week)==this.chose_week  && this.display_year==this.chose_year){
                return "calendar_chose"
            }
        },
        update_chose_week(current_week){
            this.display_year = this.chose_year;
            this.chose_week = parseInt(current_week);
            this.get_week_todos();
        },
        update_year(i){
            if (i==-1){
                this.chose_year--;
            }else{
                this.chose_year++;
            }
        },
        get_month_bg(current_month){
            var month = this.get_month();
            var year = this .get_year();
            if (year==this.chose_year && parseInt(current_month)==month){
               return "calendar_current"
            }else if(parseInt(current_month)==this.chose_month  && this.display_year==this.chose_year){
                return "calendar_chose"
            } 
            
        },
        update_chose_month(current_month){
            this.display_year = this.chose_year;
            this.chose_month = parseInt(current_month);
            this.get_month_todos();
        },
        get_todo_count(){
            var count = 0;
            for (var todo of this.display_todo){
                if (todo.state == "todo"){
                    count += 1
                }
            };
            return count
        },
        nav_select_bg(select){
            if (select==this.todo_type){
                return "bg_dark"
            }
        }
    },
    watch: {
        chose_year(){
            if (this.todo_type == "year"){
                this.get_year_todos()
            }
        },
    },
    components: {
        Calendar,
        // mavonEditor
    },
    filters:{
        levelOut(oldvalue){
            return oldvalue=="a"?"A":oldvalue=="b"?"B":oldvalue=="c"?"C":"D"
        }
    },
    created(){
        getIndexTodos().then(result=>{
            if (result.code==200){
                this.day_todo = result.day;
                this.week_todo = result.week;
                this.month_todo = result.month;
                this.year_todo = result.year;
                this.display_todo = this.day_todo;
            }else if(result.code==10202){
                alert('会话已过期,请重新登陆');
                localStorage.removeItem('ytoken');
                localStorage.removeItem('user_id');
                this.$router.push({name:'Index'})
            }else{
                alert(result.error);
            }
        })
    }
}
</script>
<style scoped>
#todo_header{
    position: fixed;
    height: 40px;
    width: 60%;
    margin-left:80px;
    top:0;
    z-index: 100;
    line-height: 40px;
    color: #f5f5f5;
}
#todo_header .first_menu{
    padding: 0 8px;
    font-size: 0.9rem;
}
#todo_header .first_menu:hover{
    background-color: rgba(0, 0, 0, 0.4);
    cursor: pointer;
}
#todo_header .first_menu+.menu{
    margin-left: 10px;
}
#todo_header .first_menu .second_menu{
    margin: 0 -8px;
}
#todo{
    width: 100%;
    height: 100%;
    background: #b4daf0;
}
#todo_body{
    width: 1250px;
    background: rgba(255, 255, 255, 0.2);
    margin: 0 auto;
    height: 100%;
    padding-top: 40px;
}
.body_left{
    width: 900px;
    float: left;
    height: 100%;
    margin-top:0;
    /* border: 1px solid red; */
}
.body_right{
    position: relative;
    float: left;
    width: 330px;
    height: 100%;
    margin-left: 10px;
    /* border: 1px solid blue; */
}
.my_calendar{
    margin-top:25px;
    height: 360px;
    border-radius: 3px;
    background-color: rgba(0, 0, 0, 0.5);
}
.calendar_header{
    height: 50px;
    /* border: 1px solid red; */
    text-align: center;
    color: #fff;
    line-height: 50px;
}
.calendar_header_left{
    margin-top: 20px;
    margin-left: 10px;
    height: 12px;
    width: 12px;
    border-top:2px solid #fff;
    border-left: 2px solid #fff;
    transform: rotate(-45deg);
}
.calendar_header_right{
    margin-top: 20px;
    margin-right: 10px;
    height: 12px;
    width: 12px;
    border-top:2px solid #fff;
    border-right: 2px solid #fff;
    transform: rotate(45deg);
}
.calendar_header_middle{
    font-size: 1.25rem;
}
.calendar_body{
    font-size: 1rem;
    color: #fff;
    /* padding: 2px 2px; */
}
.week_body{
    float: left;
    width: 40px;
    height: 40px;
    text-align: center;
    line-height: 40px;
}
.month_body{
    float: left;
    width: 80px;
    height: 80px;
    line-height: 80px;
    text-align: center;
    font-size: 2rem;
}
.calendar_day{
    background: rgba(0, 0, 0, 0.2);
}
.calendar_week{
    height: 360px;
}
.calendar_month{
    height: 320px;
}
.calendar_year{
    height: 80px;
}
.body_left .todo_action{
    flex-wrap: wrap;
}
.body_top{
    line-height: 40px;
}
.todo_action>.card{
    margin:20px 32px;
    height: 150px;
    color: #fff;
    background-color: rgba(0, 0, 0, 0.5);
    transition: all 0.2s;
}
.todo_action>.card:hover{
    cursor: pointer;
    transform: scale(1.1);
}
.todo_action>.card:nth-child(1){
    background-color: #fff;
    box-shadow: 0 0 10px 0 #937bd5;
}
.add_todo>span{
    font-size: 3rem;
    color:rgba(0, 0, 0, 0.15);    
}
.todo_conclusion{
    height: 150px;
    margin-top:10px;
    box-shadow: 0 0 5px 0px #fff;
}
.todo_conclusion>.card{
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    color: #fff;
    border-radius: 1px;
    font-family: "华文细黑","STHeiti","MingLiu";
}
.radio_label{
    cursor: pointer;
    color: #f5f5f5;
    background: rgba(0, 0, 0, 0.4);
    padding: 0 10px;
    border-radius: 5px;
}
.todo_count{
    background-color: #ffc107;
    color: #f5f5f5;
    font-size: 14px;
    padding: 0 8px;
    margin-left:5px;
    border-top-left-radius: 50%;
    border-top-right-radius: 50%;
    border-bottom-left-radius: 50%;
}
.completed{
    box-shadow: 0 0 10px 5px #28a745;
}
.no_completed{
    box-shadow: 0 0 10px 5px #dc3545;
}
#update_todo{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.2);
    z-index: 1000;
    transition: all 0.5s;
}
#update_todo>.update_content{
    width: 24%;
    height: 400px;
    margin: 140px auto;
    padding: 25px 40px;
    background-color: #fff;
    border-radius: 5px;
    font-size: 15px;
    color: #444;
}
.btn_update{
    border: 1px solid #dc3545;
    padding-left: 2rem;
    padding-right: 2rem;
    transition: all 0.25s;
}
.btn_update:hover{
    background-color: #dc3545;
    color: #fff;
}
#add_todo{
    position: fixed;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.2);
    z-index: 1000;
    transition: all 0.5s;
}
#add_todo>.add_content{
    width: 24%;
    height: 400px;
    margin: 140px auto;
    padding: 25px 40px;
    background-color: #fff;
    border-radius: 5px;
    font-size: 15px;
    color: #444;
}
.btn_add{
    border: 1px solid #dc3545;
    padding-left: 2rem;
    padding-right: 2rem;
    transition: all 0.25s;
}
.btn_add:hover{
    background-color: #dc3545;
    color: #fff;
}
.close_add_todo{
    position: absolute;
    left: 61.8%;
    top: 110px;
    width: 30px;
    height: 30px;
    line-height: 24px;
    font-size: 1.5rem;
    text-align: center;
    color: #fff;
    border: 1px solid #fff;
    border-radius: 50%;
}
.close_add_todo:hover{
    cursor: pointer;
}
.cursor_pointer:hover{
    cursor: pointer;
}
.calendar_current{
    background: #fff;
    color: #444;
    border-radius: 50%;
}
.calendar_chose{
    background: green !important;
    border-radius: 50%;
}
.calendar_pointer:hover{
    background: #71c7a5;
}
.bg_dark{
    background: rgba(0, 0, 0, 0.2);
}
</style>