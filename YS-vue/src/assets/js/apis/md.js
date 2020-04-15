import axios from "axios"
import {baseURL} from "../config.js"

function createArticle(data){
    return new Promise(
        function(resolve, reject){
            var ytoken = localStorage.getItem('ytoken');
            axios.post(baseURL+"/topics",data,{
                headers:{
                    "Authorization": ytoken
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}
function createImage(data){
    return new Promise(
        function(resolve,reject){
            var ytoken = localStorage.getItem('ytoken');
            axios.post(baseURL+"/topics/image",data,{
                headers:{
                    'Authorization':ytoken,
                    "Content-Type": "multipart/form-data"
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}
export {
    createArticle,
    createImage
}