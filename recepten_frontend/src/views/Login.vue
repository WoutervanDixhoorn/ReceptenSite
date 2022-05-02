<template>
  <b-container fluid>
    <b-form-input v-model="username" placeholder="Username" type="text"></b-form-input>
    <b-form-input v-model="password" placeholder="Password" type="password"></b-form-input>
    <b-button @click="login">Login</b-button>
  </b-container>
</template>

<script>
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
                this.$router.push({ name: 'Home' })
            })
            .catch(err => {
                console.log(err);
                //Todo: Make form validation!
            })
        }
    }
}
</script>

<style>

</style>