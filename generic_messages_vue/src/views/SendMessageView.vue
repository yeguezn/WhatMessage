<script setup lang="ts">
    import SelectContacts from '@/components/SelectContacts.vue'
    import DependentDropdown from '@/components/DependentDropdown.vue'
    import { useSendMessageStore } from "@/stores/sendMessage"
    import BaseForm from '@/components/BaseForm.vue'
    import type { formOptions } from '@/types/formOptions'
    import { useAuthStore } from '@/stores/auth'
    import ShowValidationErrors from '@/components/ShowValidationErrors.vue'
    import { onMounted } from 'vue'

    const { submitForm, setPath, errors } = useSendMessageStore()
    const { setAuthorizationHeader } = useAuthStore()

    const options:formOptions = {
        pageName:"Send message",
        submitAction:submitForm,
        submitBtnName:"Send message",
        alternativeOptionName:null,
        alternativeOptionPath:null
    }

    setAuthorizationHeader()

    setPath("/api/v1/send-message/")

    onMounted(()=>{

        document.title = "Send Message"

    })

</script>

<template>

    <ShowValidationErrors v-if="errors.length > 0" 
    class="mx-auto my-5" width="600" :errors="errors"/>
    
    <BaseForm :options="options">
        <SelectContacts></SelectContacts>
        
        <DependentDropdown></DependentDropdown>
    </BaseForm>

</template>