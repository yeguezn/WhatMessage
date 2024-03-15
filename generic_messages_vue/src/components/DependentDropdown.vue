<script setup lang="ts">
    import { reactive, ref } from 'vue'
    import axios from 'axios'
    import { useSendMessageStore } from '@/stores/sendMessage'
    import { validationRules } from '@/validations';

    const categories:Array<object> = reactive([])
    const messages:Array<object> = reactive([])
    const selectedCategory = ref("")
    const { errors, formData } = useSendMessageStore()

    function initializeCategories(){
        axios.get("/api/v1/all-categories/").then(response=>{
            for (let index = 0; index < response.data["categories"].length; index++) {
                
                categories.push(response.data["categories"][index])
    
            }
    
        }).catch(error=>{
            console.log(error.response.data)
        })
    }

    initializeCategories()

    function getMessagesByCategory(){
        
        messages.length = 0
        formData.chosenMessage = ""
        
        axios.get(`/api/v1/messagesByCategory/${selectedCategory.value}`)
        .then(response=>{

            for (let index = 0; index < response.data.length; index++) {
                
                messages.push(response.data[index])
                
            }
            
        }).catch(error=>{
            errors.push("Technical issues, please try it again later.")
        })
    }

</script>

<template>
    
    <v-select :items="categories" item-title="name" label="Choose a category"
    item-value="id" v-model="selectedCategory" @update:model-value="getMessagesByCategory">
        <template v-slot:item="{ props }">
            <v-list-item v-bind="props">
            </v-list-item>
        </template>
    </v-select>

    <v-select :items="messages" :disabled="messages.length === 0" 
    label="Choose a message" v-model="formData.chosenMessage"
    item-title="content" item-value="content" :rules="[validationRules.required]">
        
        <template v-slot:item="{ props, item }">
            <v-list-item v-bind="props">
            </v-list-item>
        </template>

    </v-select>

</template>