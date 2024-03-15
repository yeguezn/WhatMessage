<script setup lang="ts">
    import axios from 'axios'
    import { useAuthStore } from '@/stores/auth'
    import { useContactsStore } from '@/stores/contacts'

    const props = defineProps<{
        contactId:number
    }>()

    const { setAuthorizationHeader } = useAuthStore()
    const { deleteContactById } = useContactsStore()

    setAuthorizationHeader()
    
    function deleteContact(){
        axios.delete(`/api/v1/delete-contact/${props.contactId}`).then(response=>{

            deleteContactById(props.contactId)
        
        }).catch(error=>{
            console.log(error.response)
        })
    }

</script>

<template>

    <v-btn @click="deleteContact" 
    icon="em em-wastebasket" title="Delete"/>

</template>