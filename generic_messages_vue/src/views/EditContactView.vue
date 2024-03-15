<script setup lang="ts">
    import { useAuthStore } from '@/stores/auth'
    import { useRoute } from 'vue-router'
    import { onMounted, reactive } from 'vue'
    import { useContactsStore } from "@/stores/contacts"
    import { ref } from 'vue'
    import BaseForm from '@/components/BaseForm.vue'
    import type { formOptions } from '@/types/formOptions'
    import { validationRules } from '@/validations'
    import ShowValidationErrors from '@/components/ShowValidationErrors.vue'
    import ResourceNotFoundContainer from '@/components/ResourceNotFoundContainer.vue'

    const { setAuthorizationHeader } = useAuthStore()
    const route = useRoute()
    const { contact, getContactById, updateContact, errors } = useContactsStore()
    const contactId = ref()
    const options:formOptions = {
        pageName:"Edit contact",
        submitAction: ()=> updateContact(contactId.value),
        submitBtnName:"Save changes",
        alternativeOptionName:null,
        alternativeOptionPath:null
    }

    setAuthorizationHeader()

    onMounted(()=>{
        errors.length = 0
        document.title = "Edit contact"
        contactId.value = Number(route.params.contactId)
        getContactById(contactId.value)
    })

</script>

<template>

    <ResourceNotFoundContainer
    v-if="errors.length > 0 && errors[0] === 'This contact doesn\'t exist.'">

        <h1 class="text-center title text-green">{{ errors[0] }}</h1>
        <h2 class="text-center text-h3 mt-5">🙅‍♂️</h2>

    </ResourceNotFoundContainer>

    <ShowValidationErrors 
    v-if="errors.length > 0 && errors[0] !== 'This contact doesn\'t exist.'" 
    :errors="errors" class="mx-auto mt-5" width="600"/>

    <BaseForm :options="options" v-if="errors[0] !== 'This contact doesn\'t exist.'">
        <v-text-field label="Name" 
        v-model="contact.fullName" type="text"
        :rules="[validationRules.required]"/>

        <v-text-field label="Phone number" type="text"
        v-model="contact.phoneNumber"
        :rules="[validationRules.required, validationRules.phoneNumber]"/>
    </BaseForm>

</template>

<style scoped>

    .title{

        font-family:Helvetica, sans-serif;
        font-size: 50px;

    }

</style>