<script setup lang="ts">

    import router from '@/router'

    function goBackHome(){
        router.push("/")
    }


</script>

<template>
    <v-btn width="100" class="mt-10" @click="goBackHome"
        color="green">
            Go back
    </v-btn>
</template>