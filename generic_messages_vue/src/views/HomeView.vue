<script setup lang="ts">
    import SendMessageDemo from '@/components/SendMessageDemo.vue'
    import { onMounted } from 'vue'

    onMounted(()=>{
        document.title = "WhatMessage"
    })
</script>

<template>
    <h1 class="text-center mt-5 text-green mb-5 head-title">
        Do you have nothing to say?
    </h1>

    <h2 class="body-2 text-center mt-5 text-green head-title">
        We can fix that 😉
    </h2>

    <v-alert icon="em em-thinking_face"
    type="success" width="420" class="mx-auto mt-4 alert-font">

        <v-alert-title>
            What is this app about?
        </v-alert-title>

        <v-alert-text>
            This app offers predefined messages that
            you can send to your friends via Whatsapp. These messages
            are categorized, so you can choose all of
            kind of messages (Love, Motivational, Movie phrases).
        </v-alert-text>

    </v-alert>
    
    <SendMessageDemo/>

</template>

<style scoped>

    .head-title, .alert-font{
        font-family: Helvetica, sans-serif;
    }
    
</style>