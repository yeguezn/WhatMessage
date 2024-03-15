<script setup lang="ts">
    import { onMounted } from 'vue'
    import {useAuthStore} from "../stores/auth"
    import { validationRules } from '@/validations'
    import ShowValidationErrors from '@/components/ShowValidationErrors.vue'
    import BaseForm from '@/components/BaseForm.vue'
    import type { formOptions } from '@/types/formOptions'

    const {
        setAuthorizationHeader, 
        submitSigninForm, 
        formData,
        loginErrors
    } = useAuthStore()

    setAuthorizationHeader()

    onMounted(()=>{
        document.title = "Sign in"
    })

    const options:formOptions = {
        pageName:"Login", 
        submitAction:submitSigninForm,
        submitBtnName:"Login",
        alternativeOptionPath:"/signup",
        alternativeOptionName:"Create an account"
    }

</script>

<template>

    <ShowValidationErrors v-if="loginErrors.length > 0" 
    class="mx-auto mt-5" width="600" :errors="loginErrors"/>
    
    <BaseForm :options="options">
        <v-text-field label="Email" variant="outlined" 
        type="email" v-model="formData.email" 
        :rules="[validationRules.required, validationRules.email]"/>
        
        <v-text-field label="Password" variant="outlined" 
        type="password" v-model="formData.password"
        :rules="[validationRules.required]"/>

    </BaseForm>

</template>