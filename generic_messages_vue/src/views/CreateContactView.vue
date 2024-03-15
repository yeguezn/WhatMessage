<script setup lang="ts">
    import { onMounted, reactive } from 'vue'
    import { useAuthStore } from '@/stores/auth'
    import { useContactsStore } from '@/stores/contacts'
    import BaseForm from '@/components/BaseForm.vue'
    import type { formOptions } from '@/types/formOptions'
    import { validationRules } from '@/validations'
    import ShowValidationErrors from '@/components/ShowValidationErrors.vue'

    const { setAuthorizationHeader } = useAuthStore()
    const { contact, createContact, errors } = useContactsStore()

    setAuthorizationHeader()

    const options:formOptions = {
        pageName:"New contact",
        submitBtnName:"Save contact",
        submitAction:createContact,
        alternativeOptionName:null,
        alternativeOptionPath:null
    }

    onMounted(()=>{
        document.title = "New Contact"
    })

</script>

<template>

    <ShowValidationErrors :errors="errors"
    v-if="errors.length > 0" class="mx-auto mt-5" width="600"/>

    <BaseForm :options="options">
        
        <v-text-field label="Name" variant="outlined"
        type="text" v-model="contact.fullName"
        :rules="[validationRules.required]"/>

        <v-text-field label="Phone number" variant="outlined"
        type="text" v-model="contact.phoneNumber"
        :rules="[validationRules.required, validationRules.phoneNumber]"/>

    </BaseForm>

</template>