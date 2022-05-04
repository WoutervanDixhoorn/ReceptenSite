<template>
    <div>
        <h1>Navbar! Logged in as: {{this.$store.state.account.username}}</h1>
        <div v-if="this.$router.currentRoute.path != '/login'">
            <input type="button" value="Logout" @click="logout" v-if="this.$store.getters.loggedIn">
            <input type="button" value="Login" @click="login" v-else>
        </div>
    </div>
</template>

<script>
export default {
    methods: {
        logout()
        {
            this.$store.dispatch('userLogout')
            .then(() =>{
                if(this.$router.currentRoute.path != '/recepten')
                this.$router.push({name: 'ReceptenMain'})
            })
            .catch(err => {
                console.log(err)
            })
        },
        login()
        {
            this.$router.push({ name: 'Login' })     
        }
    },
}
</script>

<style scoped>
</style>