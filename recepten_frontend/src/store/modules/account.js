import { getAPI } from '../../axios-api'

export default {

state: {
    username: null,
    email: null,
    accessToken: null,
    refreshToken: null,
},

mutations: {
    updateStorage (state, { username, email, access, refresh }) {
        state.username = username
        state.email = email
        state.accessToken = access
        state.refreshToken = refresh
    },
    destroyAccount (state) {
        state.username = null
        state.email = null
        state.accessToken = null
        state.refreshToken = null
    }
},

getters: {
    loggedIn (state) {
        return state.accessToken != null
    }
},

actions: {
    userLogout (context) {
        if (context.getters.loggedIn) {
            context.commit('destroyAccount')
            getAPI.post('/recepten/logout')
        }
    },
    userLogin (context, usercredentials) {
        return new Promise((resolve, reject) => {
            getAPI.post('/recepten/login', {
                username: usercredentials.username,
                password: usercredentials.password
            })
            .then(response => {
              context.commit('updateStorage', { username: response.data.username, email: response.data.email, access: response.data.access, refresh: response.data.refresh }) 
              resolve()
            })
            .catch(err => {
              reject(err)
            })
        })
    }
},

}