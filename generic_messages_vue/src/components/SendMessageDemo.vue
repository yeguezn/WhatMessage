<script setup lang="ts">
    import DependentDropdown from "@/components/DependentDropdown.vue"
    import { useSendMessageStore } from "@/stores/sendMessage"
    import BaseForm from "./BaseForm.vue"
    import type { formOptions } from "@/types/formOptions"
    import { validationRules } from "@/validations"
    import ShowValidationErrors from "./ShowValidationErrors.vue"

    const { errors, formData, submitForm, setPath } = useSendMessageStore()

    setPath("/api/v1/send-message-demo/")

    const options:formOptions = {
        pageName:"Try it out 🙈",
        submitBtnName:"Send message",
        submitAction:submitForm,
        alternativeOptionName:null,
        alternativeOptionPath:null
    }

</script>

<template>
    
    <ShowValidationErrors v-if="errors.length > 0"
    :errors="errors" class="mt-5"/>
    
    <BaseForm :options="options">
        <v-text-field label="Phone number" variant="outlined" 
        type="text" v-model="formData.phoneNumber" 
        :rules="[validationRules.required, validationRules.phoneNumber]"
        placeholder="example: +1-202-555-0156"/>
        <DependentDropdown/>
    </BaseForm>

</template>./ShowValidationErrors.vue
