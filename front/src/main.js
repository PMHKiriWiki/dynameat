import { createApp } from 'vue'
import Axios from 'axios'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/bootstrap.min.css'
// import './assets/bootstrap.bundle.min.js'
/* import the fontawesome core */

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'


const app = createApp(App).use(store).use(router)
app.config.globalProperties.$axios = Axios
app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')
