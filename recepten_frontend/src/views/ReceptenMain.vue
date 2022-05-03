<script>
import { getAPI }  from '../axios-api'
import { mapState } from 'vuex'

import Navbar from '../components/Navbar.vue'
import Recept from '../components/Recept.vue'

export default {
    components: {
        Navbar,
        Recept,
    },
    computed: mapState(['APIData']),
    created(){
        getAPI.get('/recepten/', {
            headers: { Authorization: `Bearer ${this.$store.state.account.accessToken}`}
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
        <Navbar />
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