<script setup lang="ts">
    import { onMounted } from 'vue'
    import ResourceNotFoundContainer from "@/components/ResourceNotFoundContainer.vue"

    onMounted(()=>{

        document.title = "Not Found"

    })

</script>


<template>

    <ResourceNotFoundContainer>

        <h1 class="text-center title text-green">Page not found</h1>
        <h2 class="text-center text-h3 mt-5">🤖 4️⃣ 0️⃣ 4️⃣</h2>

    </ResourceNotFoundContainer>

</template>

<style scoped>

    .title{

        font-family:Helvetica, sans-serif;
        font-size: 50px;

    }

</style>