<script>
import { getAPI }  from '../axios-api'

import Recept from '../components/Recept.vue'

export default {
    data(){
        return{
            APIData: []
        }
    },
    created(){
        getAPI.get('/recepten/')
        .then(response => {
            this.APIData = response.data;
        })
        .catch(err => {
            console.log(err);
        });
    },
    components: {
        Recept,
    }
}
</script>

<template>
    <div>
        <h1>Recepten</h1>
        <div v-for="recept in APIData" :key="recept.id">
            <Recept :title=recept.title :content=recept.content />
        </div>
    </div>
</template>

<style scoped>
.msg {
    color: #257cff;
}
</style>