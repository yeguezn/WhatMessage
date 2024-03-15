import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives
})

axios.defaults.baseURL = "http://0.0.0.0:8000"

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(axios)
app.use(vuetify)

app.mount('#app')
