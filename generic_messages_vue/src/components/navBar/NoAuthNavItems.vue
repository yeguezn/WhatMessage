<script setup lang="ts">
    import { RouterLink } from 'vue-router'
    import SignUpBtn from './SignUpBtn.vue'

</script>

<template>

    <RouterLink to="/">

        <v-btn class="text-white" prepend-icon="em em-house">
            Home
        </v-btn>

    </RouterLink>

    <SignUpBtn/>

</template>