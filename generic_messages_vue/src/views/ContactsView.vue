<script setup lang="ts">
    import { useAuthStore } from "@/stores/auth"
    import { useContactsStore } from "@/stores/contacts"
    import DeleteBtn from "@/components/DeleteBtn.vue"
    import EditBtn from "@/components/EditBtn.vue"
    import { onMounted } from "vue"

    const { setAuthorizationHeader } = useAuthStore()
    const { initializeContacts, contacts } = useContactsStore()

    setAuthorizationHeader()

    onMounted(()=>{

        document.title = "All Contacts"
        initializeContacts()
    })

</script>

<template>
    <div class="d-flex align-center flex-column">

        <h1 v-if="contacts.length === 0" 
        class="text-center title text-green mt-5">
            You do not contacts yet.
        </h1>
        <h2 v-if="contacts.length === 0"
        class="text-center text-h3 mt-5">
            🤷‍♂️
        </h2>

        <v-card v-for="contact in contacts" 
        variant="tonal" class="d-flex align-center flex-column my-4"
        width="300" color="green" v-if="contacts.length > 0">

            <v-card-title>
                {{ contact.full_name }}
            </v-card-title>

            <v-card-subtitle>
                {{ contact.phone_number }}
            </v-card-subtitle>

            <v-card-actions>
                <EditBtn :contactId="contact.id"/>
                <DeleteBtn :contactId="contact.id"/>
            </v-card-actions>

        </v-card>

    </div>
</template>

<style scoped>

    .title{

        font-family:Helvetica, sans-serif;
        font-size: 50px;

    }

</style>