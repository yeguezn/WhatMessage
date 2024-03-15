<script setup lang="ts">
    import router from '@/router'

    defineProps<{
        contactId:number
    }>()

    function EditContact(contactId:number){
        router.push({
            name:"edit-contact",
            params:{
                contactId:contactId
            }
        })
    }

</script>

<template>

    <v-btn @click="EditContact(contactId)"
    icon="em em-pencil2" title="Edit"/>

</template>