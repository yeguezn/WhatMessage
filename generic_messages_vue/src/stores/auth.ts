import { defineStore } from 'pinia'
import { ref, reactive } from 'vue'
import axios from 'axios'

export const useAuthStore = defineStore("auth", ()=>{
    const isAuthenticated = ref(false)
    const token = ref("")
    const formData = reactive({
        email:"",
        password:""
    })
    const loginErrors:Array<string> = reactive([])

    function initializeStore(){
        
        if (localStorage.getItem("token")) {

            token.value = `${localStorage.getItem("token")}`
            isAuthenticated.value = true
        
        }else{
            token.value = ""
            isAuthenticated.value = false
        }
    }

    function setAuthorizationHeader(){

        if(token.value){
        
            axios.defaults.headers.common["Authorization"] = "Token " + token.value
        
        }else{
            
            axios.defaults.headers.common["Authorization"] = ""
        
        }
    }

    function signin(token:string){
        setToken(token)
        axios.defaults.headers.common["Authorization"] = "Token " + token
        localStorage.setItem("token", token)
        window.location.href = "/send-message"
    }

    function setToken(authToken:string){
        token.value = authToken
        isAuthenticated.value = true
    }

    function removeToken(){
        token.value = ""
        isAuthenticated.value = false
    }

    function submitSigninForm(){

        axios.defaults.headers.common["Authorization"] = ""
        localStorage.removeItem("token")

        const data = {
            email:formData.email,
            password:formData.password
        }

        loginErrors.length = 0
        
        axios.post("/api/v1/signin/", data).then(response=>{

            signin(response.data.token)

        }).catch(error=>{

            if (error.response) {

                for (const property in error.response.data) {

                    loginErrors.push(error.response.data[property])
                }
                
            }else{
                loginErrors.push("Technical issues, please try again later.")
            }
        })
        
    }

    return {
        token, 
        initializeStore, 
        setToken, 
        removeToken, 
        isAuthenticated,
        signin,
        submitSigninForm,
        formData,
        loginErrors,
        setAuthorizationHeader
    }
})