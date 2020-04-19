import axios from 'axios'
import {baseURL} from '../config'


function getFollow(u_id){
    return new Promise(
        function(resolve, reject){
            axios.get(baseURL+"/users/follow/"+u_id).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function createAvatar(u_id, data){
    return new Promise(
        function(resolve, rejcet){
            var ytoken = localStorage.getItem('ytoken');
            axios.post(baseURL+'/users/'+u_id+"/avatar",data,{
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

function putUserInfo(u_id, data){
    return new Promise(
        function(resolve, reject){
            var ytoken = localStorage.getItem('ytoken');
            axios.put(baseURL+"/users/"+u_id, data,{
                headers:{
                    'Authorization':ytoken,
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}

export{
    getFollow,
    createAvatar,
    putUserInfo,
}