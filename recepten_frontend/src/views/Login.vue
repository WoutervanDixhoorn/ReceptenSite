<template>
<div>
    <Navbar />
    <div class="loginForm">
        <input type="text" v-model="username" placeholder="Username">
        <input type="password" v-model="password" placeholder="Password">
        <input type="button" value="Login" @click="login">
    </div>
</div>
</template>

<script>
import Navbar from '../components/Navbar.vue'

export default {
    data() {
        return {
            username: '',
            password: ''
        }
    },
    methods: {
        login()
        {
            this.$store.dispatch('userLogin', {
                username: this.username,
                password: this.password
            })
            .then(() => {
                this.$router.push({ name: 'ReceptenMain' })
            })
            .catch(err => {
                console.log(err);
                //Todo: Make form validation!
            })
        }
    },
    components: {
        Navbar,
    }
}
</script>

<style>

</style>