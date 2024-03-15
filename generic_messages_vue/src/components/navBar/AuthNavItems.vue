<script setup lang="ts">
    import { RouterLink } from 'vue-router'
    import router from '@/router'
    import { useAuthStore } from '@/stores/auth'
    import axios from 'axios'

    const { removeToken } = useAuthStore()

    function openPage(pagePath:string){
        router.push(pagePath)
    }

    function logout() {
        localStorage.removeItem("token")
        removeToken()
        axios.defaults.headers.common["Authorization"] = ""
        window.location.href = "/login"
    }

</script>

<template>

    <v-menu open-on-hover>

        <template v-slot:activator="{ props }">
            <v-btn class="text-white" v-bind="props" prepend-icon="em em-busts_in_silhouette">
                Contacts
            </v-btn>
        </template>

        <v-list>
            <v-list-item @click="openPage('/new-contact')">
                Create contact
            </v-list-item>

            <v-list-item @click="openPage('/get-contacts')">
                All contacts
            </v-list-item>
        </v-list>

    </v-menu>

    <RouterLink to="/send-message">

        <v-btn class="text-white" prepend-icon="em em-speech_balloon">
            Send message
        </v-btn>
    
    </RouterLink>

    <RouterLink to="/history">

        <v-btn class="text-white" prepend-icon="em em-clock2">
            History
        </v-btn>

    </RouterLink>

    <v-btn class="text-white" prepend-icon="em em-door" @click="logout">
        Logout
    </v-btn>

</template>