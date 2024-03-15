<script setup lang="ts">
    import { useAuthStore } from '@/stores/auth'
    import { useHistoryStore } from '@/stores/history'
    import { onMounted } from 'vue'
    import HistoryTable from "@/components/HistoryTable.vue"
    import FilterHistory from '@/components/FilterHistory.vue'
    import ShowValidationErrors from '@/components/ShowValidationErrors.vue'

    const { setAuthorizationHeader } = useAuthStore()
    const { getHistory, errors } = useHistoryStore()

    setAuthorizationHeader()

    onMounted(()=>{
        
        document.title = "History"
        getHistory()

    })

</script>

<template>
    <ShowValidationErrors v-if="errors.length > 0" :errors="errors"
    class="mx-auto mt-5" width="600"/>

    <FilterHistory class="mt-10"/>
    <div class="d-flex align-center justify-center container">
        <HistoryTable/>
    </div>
</template>

<style scoped>
    .container{
        height:390px;
    }
</style>