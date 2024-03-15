<script setup lang="ts">
    import type { formOptions } from '@/types/formOptions'

    defineProps<{
        options:formOptions
    }>()

</script>

<template>

    <v-sheet class="mx-auto d-flex justify-center flex-column" 
    width="300" height="500">

        <h1 class="text-center mb-4 head-title text-green">{{ options.pageName }}</h1>
        
        <v-form @submit.prevent="options.submitAction" 
        class="d-flex justify-center flex-column">

            <slot></slot>

            <v-btn color="success" type="submit">
                {{ options.submitBtnName }}
            </v-btn>

        </v-form>

        <p class="d-flex justify-center ga-2 mt-2" v-if="options.alternativeOptionPath">
            or <RouterLink :to="options.alternativeOptionPath" 
            class="text-decoration-none">
                {{ options.alternativeOptionName }}
            </RouterLink>
        </p>
    
    </v-sheet>

</template>

<style scoped>
    .head-title{
        font-family: Helvetica, sans-serif;
    }
</style>