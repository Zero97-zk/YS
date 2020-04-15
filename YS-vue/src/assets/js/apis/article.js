import axios from "axios"
import {baseURL} from "../config"

function getArticle(t_id){
    return new Promise(
        function (resolve, reject){
            var ytoken = localStorage.getItem("ytoken");
            axios.get(baseURL+"/topics/t_id/"+t_id,{
                headers: {
                    'Authorization': ytoken
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}
function getUserInfo(u_id){
    return new Promise(
        function (resolve, reject){
            axios.get(baseURL+"/users/"+u_id).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function getFans(u_id){
    return new Promise(
        function (resolve, reject){
            axios.get(baseURL+"/users/fans/"+u_id).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function createFollow(followed_id){
    return new Promise(
        function (resolve, reject){
            var ytoken = localStorage.getItem("ytoken");
            axios.post(baseURL+"/users/follow/"+followed_id,{},{
                headers: {
                    'Authorization': ytoken
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}
function deleteFollow(followed_id){
    return new Promise(
        function (resolve, reject){
            var ytoken = localStorage.getItem("ytoken");
            axios.delete(baseURL+"/users/follow/"+followed_id,{
                headers: {
                    'Authorization': ytoken
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}
function getMessages(t_id){
    return new Promise(
        function (resolve, reject){
            axios.get(baseURL+"/messages/t_id/"+t_id).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function createMessage(data){
    return new Promise(
        function (resolve, reject){
            var ytoken = localStorage.getItem("ytoken");
            axios.post(baseURL+"/messages",data,{
                headers:{
                    'Authorization': ytoken
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function createReply(data){
    return new Promise(
        function (resolve, reject) {
            var ytoken = localStorage.getItem("ytoken");
            axios.post(baseURL+"/messages/reply",data,{
                headers:{
                    'Authorization': ytoken
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function getAuthorArticles(author_id) {
    return new Promise(
        function (resolve, reject){
            var ytoken = localStorage.getItem("ytoken");
            axios.get(baseURL+"/topics/u_id/"+author_id,{
                headers:{
                    'Authorization': ytoken
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function createCollection(data) {
    return new Promise(
        function (resolve, reject) {
            var ytoken = localStorage.getItem("ytoken");
            axios.post(baseURL+"/topics/collect",data,{
                headers: {
                    'Authorization': ytoken
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function getCollections(u_id) {
    return new Promise(
        function (resolve, reject) {
            var ytoken = localStorage.getItem("ytoken");
            axios.get(baseURL+"/topics/collect/u_id/"+u_id,{
                headers: {
                    'Authorization': ytoken
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function deleteCollection(t_id) {
    return new Promise(
        function (resolve, reject) {
            var ytoken = localStorage.getItem("ytoken");
            axios.delete(baseURL+"/topics/collect/t_id/"+t_id,{
                headers:{
                    'Authorization': ytoken  
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function createLike(data) {
    return new Promise(
        function (resolve, reject) {
            var ytoken = localStorage.getItem("ytoken");
            axios.post(baseURL+"/topics/like",data,{
                headers: {
                    'Authorization': ytoken
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function getLikes(t_id) {
    return new Promise(
        function (resolve, reject) {
            var ytoken = localStorage.getItem("ytoken");
            axios.get(baseURL+"/topics/like/t_id/"+t_id,{
                headers: {
                    'Authorization': ytoken
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function deleteLike(t_id) {
    return new Promise(
        function (resolve, reject) {
            var ytoken = localStorage.getItem("ytoken");
            axios.delete(baseURL+"/topics/like/t_id/"+t_id,{
                headers:{
                    'Authorization': ytoken  
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function createWatch(data) {
    return new Promise(
        function (resolve, reject) {
            var ytoken = localStorage.getItem("ytoken");
            axios.post(baseURL+"/topics/watch",data,{
                headers: {
                    'Authorization': ytoken
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}







export {
    getArticle,
    getUserInfo,
    getAuthorArticles,
    getFans,
    getMessages,
    getCollections,
    getLikes,
    createFollow,
    createMessage,
    createReply,
    createCollection,
    createLike,
    deleteLike,
    deleteCollection,
    createWatch,
    deleteFollow

}