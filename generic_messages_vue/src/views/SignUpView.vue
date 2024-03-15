<script setup lang="ts">
    import { reactive } from 'vue'
    import axios from "axios"
    import { onMounted } from 'vue'
    import { useAuthStore } from '@/stores/auth'
    import { validationRules } from '@/validations'
    import BaseForm from '@/components/BaseForm.vue'
    import ShowValidationErrors from '@/components/ShowValidationErrors.vue'
    import type { formOptions } from '@/types/formOptions'

    const formData= reactive({
        email:"",
        username:"",
        password:"",
        confirmPassword:""
    })

    const passwordValidation = {
        dontMatch:(value:string)=> value === formData.password || 'Passwords don\'t match.'
    }

    const errors:Array<string> = reactive([])

    const { signin } = useAuthStore()

    function submitForm(){
        errors.length = 0

        if (formData.password !== formData.confirmPassword){

            errors.push("Passwords don\'t match.")
            return
            
        }

        const data = {
            username:formData.username,
            email:formData.email,
            password:formData.password
        }

        axios.post("/api/v1/signup/", data).then(response =>{

            signin(response.data.token)
           
        
        }).catch(error=>{

            for (const property in error.response.data) {

                errors.push(error.response.data[property][0])
            }    

        })
        
    }

    onMounted(()=>{
        document.title ="Sign Up"
    })

    const options:formOptions = {
        pageName:"Sign up",
        submitBtnName:"Sign Up",
        submitAction:submitForm,
        alternativeOptionPath:"/login",
        alternativeOptionName:"Login"
    }
</script>

<template>

    <ShowValidationErrors v-if="errors.length > 0" 
    class="mx-auto my-5" width="600" :errors="errors"/>
    
    <BaseForm :options="options">
        <v-text-field label="Email" variant="outlined" 
        type="email" v-model="formData.email" 
        :rules="[validationRules.required, validationRules.email]"/>

        <v-text-field label="Username" variant="outlined" 
        type="text" v-model="formData.username" 
        :rules="[validationRules.required]"/>
        
        <v-text-field label="Password" variant="outlined" 
        type="password" v-model="formData.password"
        :rules="[validationRules.required]"/>

        <v-text-field label="Confirm password" variant="outlined" 
        type="password" v-model="formData.confirmPassword"
        :rules="[validationRules.required, passwordValidation.dontMatch]"/>
    </BaseForm>

</template>