<script setup lang="ts">
    import router from '@/router'

    function navigateTo(path:string){

        router.push(path)

    }

</script>

<template>
    <v-menu open-on-hover>
        <template v-slot:activator="{ props }">
            <v-btn v-bind:="props"
            prepend-icon="em em-bust_in_silhouette">
                Sign Up
            </v-btn>
        </template>

        <v-card class="mx-auto my-12" min-width="282"
        min-height="290" color="green">

            <v-card-title class="text-center">Sign Up</v-card-title>

            <v-card-text>
                <div class="text-center">
                    <p>If you create an account, you will be able to:</p>
                    <p>- Create contacts.</p>
                    <p>- Check the history of messages you have sent.</p>
                </div>
            </v-card-text>

            <div class="d-flex justify-center mb-4">
                <v-btn @click="navigateTo('/signup')" class="btn">
                    Sign Up
                </v-btn>
            </div>

            <v-divider class="mx-4"></v-divider>

            <v-card-title class="text-center">
                Already have an account?
            </v-card-title>

            <div class="d-flex justify-center">
                <v-btn @click="navigateTo('/login')" class="btn">
                    Sign in
                </v-btn>
            </div>
        </v-card>
        
    </v-menu>

</template>