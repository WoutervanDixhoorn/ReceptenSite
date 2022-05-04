<template>
    <div class="profile">
        <Navbar />
        <span>Username: </span>
        <a href="#">{{ this.$store.state.account.username }}</a>
        <br>
        <span>Email: </span>
        <a href="#">{{ this.$store.state.account.email }}</a>
    </div>
</template>

<script>
import Navbar from '../components/Navbar.vue'

export default {
    components: {
        Navbar,
    }
}
</script>