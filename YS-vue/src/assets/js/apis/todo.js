import axios from "axios"
import {baseURL} from "../config.js"
import qs from 'qs'

function getIndexTodos(){
    return new Promise(
        function(resolve, reject){
            var ytoken = localStorage.getItem('ytoken');
            axios.get(baseURL+'/todos',
            {
                headers:{
                    'Authorization': ytoken
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
};
function dayTodos(type, year, day, data){
    return new Promise(
        function(resolve, reject){
            var ytoken = localStorage.getItem('ytoken');
            var url = baseURL+`/todos/day`;
            var headers = {
                'Authorization': ytoken
            };
            // data = qs.stringify(data)
            if(type=="get"){
                axios.get(url+`/${year}/${day}`,{
                    headers
                }).then(result=>{
                    resolve(result.data)
                });
            }else if(type=="post"){
                axios.post(url, data,{
                    headers
                }).then(result=>{
                    resolve(result.data)
                });
            }else if(type=="put"){
                axios.put(url, data,{
                    headers
                }).then(result=>{
                    resolve(result.data)
                })
            }
            
        }
    )
};
function weekTodos(type, year, week, data=null){
    return new Promise(
        function(resolve, reject){
            var ytoken = localStorage.getItem('ytoken');
            var url = baseURL+`/todos/week`;
            var headers = {
                'Authorization': ytoken
            };
            // data = qs.stringify(data);
            if(type=="get"){
                axios.get(url+`/${year}/${week}`,{
                    headers
                }).then(result=>{
                    resolve(result.data)
                });
            }else if(type=="post"){
                axios.post(url, data,{
                    headers
                }).then(result=>{
                    resolve(result.data)
                });
            }else if(type=="put"){
                axios.put(url, data,{
                    headers
                }).then(result=>{
                    resolve(result.data)
                })
            }
            
        }
    )
};
function monthTodos(type, year, month, data=null){
    return new Promise(
        function(resolve, reject){
            var ytoken = localStorage.getItem('ytoken');
            var url = baseURL+`/todos/month`;
            var headers = {
                'Authorization': ytoken
            };
            // data = qs.stringify(data);
            if(type=="get"){
                axios.get(url+`/${year}/${month}`,{
                    headers
                }).then(result=>{
                    resolve(result.data)
                });
            }else if(type=="post"){
                axios.post(url, data,{
                    headers
                }).then(result=>{
                    resolve(result.data)
                });
            }else if(type=="put"){
                axios.put(url, data,{
                    headers
                }).then(result=>{
                    resolve(result.data)
                })
            }
            
        }
    )
};
function yearTodos(type, year, data=null){
    return new Promise(
        function(resolve, reject){
            var ytoken = localStorage.getItem('ytoken');
            var url = baseURL+`/todos/year`;
            var headers = {
                'Authorization': ytoken
            };
            // data = qs.stringify(data);
            if(type=="get"){
                axios.get(url+`/${year}`,{
                    headers
                }).then(result=>{
                    resolve(result.data)
                });
            }else if(type=="post"){
                axios.post(url, data,{
                    headers
                }).then(result=>{
                    resolve(result.data)
                });
            }else if(type=="put"){
                axios.put(url, data,{
                    headers
                }).then(result=>{
                    resolve(result.data)
                })
            }
            
        }
    )
};

export {
    getIndexTodos,
    dayTodos,
    weekTodos,
    monthTodos,
    yearTodos
}