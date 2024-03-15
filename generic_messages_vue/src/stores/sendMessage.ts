import { defineStore } from 'pinia'
import axios from "axios"
import { reactive } from 'vue'

export const useSendMessageStore = defineStore("sendMessage", ()=>{
    const errors:Array<string> = reactive([])
    
    const formData = {
        phoneNumber:"",
        chosenMessage:""
    }
    
    let path:string = ""

    function submitForm(){
        errors.length = 0
        const data = {
            phone_number:formData.phoneNumber,
            message:formData.chosenMessage
        }

        axios.post(path, data).then(response=>{

            window.open(response.data["whatsapp_url"], "_blank")

        }).catch(error=>{
    
            if (error.response.status === 400) {

                for (const property in error.response.data) {

                    errors.push(error.response.data[property][0])
                }
            
            }else{

                errors.push("Technical issues, please try again later.")
                
            }

        })
    }

    function setPath(newPath:string){
        path = newPath
    }

    return {submitForm, errors, formData, setPath}
})