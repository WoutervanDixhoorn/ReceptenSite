import { createApp } from 'vue'
import Vuex from 'vuex'
import store from './store/store.js'
import App from './App.vue'
import router from './router'

import Equal from 'equal-vue'
import 'equal-vue/dist/style.css'

//Create the store instance

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

app.use(router);
app.use(Vuex);
app.use(store);
app.use(Equal);

app.mount('#app');
