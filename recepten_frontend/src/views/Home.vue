<script>
import { getAPI }  from '../axios-api'
import { mapState } from 'vuex'

import Recept from '../components/Recept.vue'

export default {
    components: {
        Recept,
    },
    computed: mapState(['APIData']),
    created(){
        getAPI.get('/recepten/', {
            headers: { Authorization: `Bearer ${this.$store.state.accessToken}`}
        })
        .then(response => {
            this.$store.state.APIData = response.data;
        })
        .catch(err => {
            console.log(err);
        });
    },
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