<script setup lang="ts">
    import GoBackHomeBtn from "@/components/GoBackHomeBtn.vue"
</script>

<template>

    <div class="d-flex flex-column align-center">
        
        <slot></slot>
        
        <GoBackHomeBtn/>
    </div>

</template>