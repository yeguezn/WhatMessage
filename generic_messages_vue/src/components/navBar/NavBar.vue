<script setup lang="ts">
    import { useAuthStore } from '@/stores/auth'
    import AuthNavItems from './AuthNavItems.vue'
    import NoAuthNavItems from './NoAuthNavItems.vue';
    
    const { isAuthenticated } = useAuthStore()

</script>

<template>

    <v-app-bar color="green">

        <v-app-bar-title class="navbar-title font-weight-bold">
            WhatMessage
        </v-app-bar-title>
        
        <v-container class="mx-auto d-flex align flex-row">
            <v-spacer></v-spacer>
    
            <AuthNavItems v-if="isAuthenticated"></AuthNavItems>
            
            <NoAuthNavItems v-else></NoAuthNavItems>
        </v-container>
    </v-app-bar>
   
</template>

<style scoped>

    .navbar-title{
        font-family: Helvetica, sans-serif;
    }

</style>