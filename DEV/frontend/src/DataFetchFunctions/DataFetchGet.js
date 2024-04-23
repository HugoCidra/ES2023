import axios from 'axios'

const apiUrl = process.env.REACT_APP_API_URL;


/**
 * INSTALL axios
 * 
 * METHOD: GET
 * The function verify if token saved in local storage and make request
 * @param {*} url endpoint url (example:api/creators, not necessary localhost:8000)
 * @param {*} data if necessary set data
 * @returns json result with {success:"yes"/"no", data/error:data/error}
 * 
 * @creator David
 */
function DataFetchGet(url,data=null) {
    url=apiUrl + url;

    //access token saved in local storage, if not exists return null
    let token=localStorage.getItem("token")

    //with authentication
    if (token!=null){
        //not send data
        if (data==null){
            return new Promise((resolve,reject)=>{
                axios.get(url,{
                    headers:{
                        Authorization:token
                    }
                })
                .then(response=>{resolve({success:"yes",data:response['data']})})
                .catch(error=>{reject({success:"no",error:error})});
        })}
        //send data
        else{
            return new Promise((resolve,reject)=>{
                axios.get(url,{
                    headers:{
                        Authorization:token
                    },
                    params:data
                })
                .then(response=>{resolve({success:"yes",data:response['data']})})
                .catch(error=>{reject({success:"no",error:error})});
            })}
        }
    //without authentication
    else{
        //not send data
        if (data==null){
            return new Promise((resolve,reject)=>{
                axios.get(url)
                .then(response=>{resolve({success:"yes",data:response['data']})})
                .catch(error=>{reject({success:"no",error:error})});
        })}
        //send data
        else{
            return new Promise((resolve,reject)=>{
                axios.get(url,{
                    params:data
                })
                .then(response=>{resolve({success:"yes",data:response['data']})})
                .catch(error=>{reject({success:"no",error:error})});
            })}
    }
}
export default DataFetchGet;

