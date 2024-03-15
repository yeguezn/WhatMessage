<script setup lang="ts">
    import { reactive } from 'vue'
    import { useHistoryStore } from '@/stores/history'

    const { getHistoryASC, getHistoryDESC } = useHistoryStore()

    const items = reactive([
        {
            name:"Oldest",
            clickAction:() => getHistoryDESC()
        },
        
        {
            name:"Latest",
            clickAction: ()=> getHistoryASC()
        }
    ])

</script>

<template>
    
    <v-col class="mx-auto" cols="4">
        <v-select variant="outlined" label="Filter by" :items="items" 
        item-title="name">

            <template v-slot:item="{ props, item }">

                <v-list-item v-bind="props" @click="item.raw.clickAction"></v-list-item>

            </template>

        </v-select>
    </v-col>

</template>