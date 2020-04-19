import axios from 'axios'
import {baseURL} from '../config'

function getIndexArticles(){
    return new Promise(
        function(resolve, reject){
            axios.get(baseURL+'/topics').then(result=>{
                resolve(result.data)
            })
        }
    )
}

function getTagArticles(tag){
    return new Promise(
        function(resolve,reject){
            axios.get(baseURL+'/topics',{
                params:{
                    type: tag
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function getDayArticles(year,month,day){
    return new Promise(
        function(resolve,reject){
            axios.get(baseURL+'/topics/day',{
                params:{
                    year,
                    month,
                    day
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function getTitleArticles(title){
    return new Promise(
        function(resolve, reject){
            axios.get(baseURL+'/topics/title',{
                params:{
                    title
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}

function getNicknameArticles(nickname){
    return new Promise(
        function (resolve,reject) {
            axios.get(baseURL+'/topics/nickname',{
                params:{
                    nickname
                }
            }).then(result=>{
                resolve(result.data)
            })
        }
    )
}
export {
    getIndexArticles,
    getDayArticles,
    getTagArticles,
    getTitleArticles,
    getNicknameArticles
}