import axios from 'axios'
const apiUrl = process.env.REACT_APP_API_URL;
/**
 * INSTALL axios
 * 
 * Method PUT
 * 
 * The function verify if token saved in local storage and make request
 * @param {*} url endpoint url (example:api/login, not necessary localhost:8000)
 * @param {*} data  json to send to api 
 * @returns json result with {success:"yes"/"no", data/error:data/error}
 * 
 * @creator David
 */
function DataFetchPut(url,data) {
        url=apiUrl + url;

        //access token saved in local storage, if not exists return null
        let token=localStorage.getItem("token")
        
        //with authentication and send json
        if (token!=null){
            return new Promise((resolve, reject) => {
                axios.put(url,data,{
                    headers:{
                        Authorization:token
                    }
                })
                .then(response=>{resolve({success:"yes",data:response['data']})})
                .catch(error=>{reject({success:"no",error:error})});
        })
        }
        else{
            //without authentication and send json
            return new Promise((resolve,reject)=>{
                axios.put(url,data)
                .then(response=>{resolve({success:"yes",data:response['data']})})
                .catch(error=>{reject({success:"no",error:error})});
            })      
        }
}
export default DataFetchPut;

