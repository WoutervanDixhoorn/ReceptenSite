import { createApp } from 'vue'
import Vuex from 'vuex'
import store from './store/store.js'
import App from './App.vue'
import router from './router'

import { BootstrapVue3 } from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

//Create the store instance

const app = createApp(App);

app.use(router);
app.use(Vuex);
app.use(store);
app.use(BootstrapVue3);

app.mount('#app');
