import { createApp } from 'vue'
import Vuex from 'vuex'
import store from './store/store.js'
import App from './App.vue'
import router from './router'

import Equal from 'equal-vue'
import 'equal-vue/dist/style.css'

//Redirect if page is login only
router.beforeEach((to, from, next) => {
    if(to.matched.some(record => record.meta.requiresLogin)){
        if(!store.getters.loggedIn){
            next({name: 'Login'});
        } else {
            next();
        }
    } else {
        next();
    }
})

const app = createApp(App);

app.use(router); //To route

app.use(Vuex); // To store
app.use(store);

app.use(Equal); // To UI

app.mount('#app');
