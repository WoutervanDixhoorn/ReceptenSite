<script>
import { getAPI }  from '../axios-api'

import Navbar from '../components/Navbar.vue'

export default {
    data() {
        return {
        name: 'BootstrapVue',
        show: true
        }
    },
    watch: {
        show(newVal) {
        console.log('Alert is now ' + (newVal ? 'visible' : 'hidden'))
        }
    },
    methods: {
        toggle() {
        console.log('Toggle button clicked')
        this.show = !this.show
        },
        dismissed() {
        console.log('Alert dismissed')
        }
    },
    components: {
        Navbar,
    }   
}
</script>

<template>
    <div>
        <Navbar />
        <b-button size="sm" @click="toggle">
            {{ show ? 'Hide' : 'Show' }} Alert
        </b-button>
        <b-alert
            v-model="show"
            class="mt-3"
            dismissible
            @dismissed="dismissed"
        >
            Hello {{ name }}!
        </b-alert>
    </div>
</template>

<style scoped>
</style>