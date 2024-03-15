import { defineStore } from 'pinia'
import { reactive } from 'vue'
import axios from "axios"
import router from '@/router'

export const useContactsStore = defineStore("contacts", ()=>{
    const contacts:Array<object> = reactive([])
    const contact = reactive({
        fullName:"",
        phoneNumber:""
    })
    const errors:Array<string> = reactive([])

    function initializeContacts(){
        contacts.length = 0
        
        axios.get("/api/v1/get-contacts/").then(response=>{
        
            for (let index = 0; index < response.data.length; index++) {
            
                contacts.push(response.data[index])
            
            }

        }).catch(error =>{
            
            if (error.response) {

                for (const property in error.response.data) {

                    errors.push(error.response.data[property][0])
                }
                
            }else{
                errors.push("Technical issues, please try again later.")
            }
        
        })

    }

    function getContactById(contactId:number){
        axios.get(`/api/v1/get-contact/${contactId}`)
        .then(response=>{

            contact.fullName = response.data.full_name
            contact.phoneNumber = response.data.phone_number

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

    function updateContact(contactId:number){

        const data = {
            full_name: contact.fullName,
            phone_number:contact.phoneNumber
        }

        let i = contacts.map(contact=>contact.id).indexOf(contactId) 

        axios.put(`api/v1/update-contact/${contactId}`, data)
        .then(response=>{
            
            contacts[i].full_name = response.data.full_name
            contacts[i].phone_number = response.data.phone_number
            router.push("/get-contacts")
        })
        .catch(error=>{
            if (error.response) {

                for (const property in error.response.data) {

                    errors.push(error.response.data[property][0])
                }
                
            }else{
                errors.push("Technical issues, please try again later.")
            }
        })

        
    }

    function deleteContactById(contactId:number){

        let i = contacts.map(contact => contact.id).indexOf(contactId) 
        contacts.splice(i, 1)
    }

    function createContact() {

        const data = {
            full_name:contact.fullName, 
            phone_number:contact.phoneNumber
        }
        
        axios.post("/api/v1/new-contact/", data).then(response=>{

            router.push("/get-contacts")
            
        }).catch(error=>{

            if (error.response) {

                for (const property in error.response.data) {

                    errors.push(error.response.data[property][0])
                }

            }else{
                errors.push("Technical issues, please try again later.")
            }
        })
    }

    return {
        initializeContacts, 
        contacts, 
        deleteContactById,
        getContactById,
        contact,
        updateContact,
        createContact,
        errors
    }
})