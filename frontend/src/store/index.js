import Vue from 'vue'
import Vuex from 'vuex'
import activityLog from './activityLog'
import user from './user'

Vue.use(Vuex)

export default new Vuex.Store({

  modules: {
    activityLog,
    user
  },
  state: {

  },
  mutations: {

  },
  actions: {

  }

})
