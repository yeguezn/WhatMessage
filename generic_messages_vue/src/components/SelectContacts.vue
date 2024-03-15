<script setup lang="ts">
    import { useAuthStore } from '@/stores/auth'
    import { useContactsStore } from '@/stores/contacts'
    import { useSendMessageStore } from '@/stores/sendMessage'
    import { ref } from 'vue'

    const { setAuthorizationHeader } = useAuthStore()
    const { contacts, initializeContacts } = useContactsStore()
    const { formData } = useSendMessageStore()
    const phoneNumber = ref("")

    setAuthorizationHeader()

    initializeContacts()

    function selectContact(){
        formData.phoneNumber = phoneNumber.value
    }

</script>

<template>

    <v-select :items="contacts" item-title="full_name" label="Choose a contact"
    item-value="phone_number" v-model="phoneNumber" 
    @update:model-value="selectContact" variant="outlined">
        <template v-slot:item="{ props, item }">
            <v-list-item v-bind="props" :subtitle="item.raw.phone_number">
            </v-list-item>
        </template>
    </v-select>

</template>