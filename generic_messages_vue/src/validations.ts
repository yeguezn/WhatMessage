export const validationRules = {
    required: (value:string) => !!value || 'Required.',
    email: (value:string) => {
        const pattern =
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        
          return pattern.test(value) || 'Invalid e-mail.'
    },
    phoneNumber: (value:string)=>{
        const pattern = /^\+(?:[0-9] ?){6,14}[0-9]$/

        return pattern.test(value) || 'Phone number field accepts only international format.'
    }
}

