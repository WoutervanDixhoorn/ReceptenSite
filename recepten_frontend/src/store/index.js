import Vue from 'vue'
import Vuex from 'vuex'
import AccountModule from './modules/account'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    APIData: ''
  },
  modules: {
    account: AccountModule,
  }
}); 
