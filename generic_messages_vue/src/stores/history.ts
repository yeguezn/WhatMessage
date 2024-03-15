import { defineStore } from 'pinia'
import { reactive } from 'vue'
import axios from 'axios'

export const useHistoryStore = defineStore("history", ()=>{
    
    const records:Array<object> = reactive([])
    const errors:Array<string> = reactive([])

    function getHistory() {

        records.length = 0

        axios.get("/api/v1/get-history/").then(response=>{
            
            response.data.forEach((record:object) => {

                records.push(record)
                
            })
        }).catch(error=>{
            if (error.response) {

                for (const property in error.response.data) {

                    errors.push(error.response.data[property])
                }
                
            }else{
                errors.push("Technical issues, please try again later.")
            }
        })
        
    }

    function getHistoryASC() {

        records.length = 0

        axios.get("/api/v1/get-history-asc/").then(response=>{
            
            response.data.forEach((record:object) => {

                records.push(record)
                
            })
        }).catch(error=>{
            if (error.response) {

                for (const property in error.response.data) {

                    errors.push(error.response.data[property])
                }
                
            }else{
                errors.push("Technical issues, please try again later.")
            }
        })
        
    }

    function getHistoryDESC() {

        records.length = 0

        axios.get("/api/v1/get-history-desc/").then(response=>{
            
            response.data.forEach((record:object) => {

                records.push(record)
                
            })
        }).catch(error=>{
            if (error.response) {

                for (const property in error.response.data) {

                    errors.push(error.response.data[property])
                }
                
            }else{
                errors.push("Technical issues, please try again later.")
            }
        })
        
    }

    function getLocalTime(dateTime:string){
        let date = new Date(dateTime)
        return date.toLocaleTimeString()
    }

    function getLocalDate(dateTime:string){
        let date = new Date(dateTime)
        return date.toLocaleDateString()
    }

    return {
        records,
        getHistory,
        getHistoryASC,
        getHistoryDESC,
        getLocalDate,
        getLocalTime,
        errors
    }

})