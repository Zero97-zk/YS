import axios from "axios"
import {baseURL} from "../config.js"

function avoidLogin(ytoken){
    return new Promise(
        function(resolve,reject){
            axios.get(baseURL+"/users/avoid_login",{
                headers: {
                    'Authorization': ytoken
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
};
function login(data){
    return new Promise(
        function(resolve,reject){
            axios.post(baseURL+"/ytoken",data).then(result=>{
                resolve(result.data)
            })
        }
    )
};
function register(data){
    return new Promise(
        function(resolve, reject){
            axios.post(baseURL+"/users", data).then(result=>{
                resolve(result.data)
            })
        }
    )
}

export {
    avoidLogin,
    login,
    register,
}