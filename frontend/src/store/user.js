import authAPI from '@/api/user'
import router from '@/router/index'

export default {
  state: {
    current: undefined
  },
  mutations: {
    setUser (state, user) {
      state.current = user
    }
  },
  actions: {
    async getCurrentUser ({ commit }) {
      const user = await authAPI.getCurrentUser()
      if (user !== 401 && 403) {
        commit('setUser', user)
        if (localStorage.lastRoute !== 'Activity') {
          router.push('/activity')
        }
      } else {
        console.log(localStorage.lastRoute)
        if (!localStorage.lastRoute === 'SignIn') {
          router.push('/')
        }
        commit('setUser', undefined)
      }
    },

    async login ({ commit }, credentials) {
      await authAPI.login(credentials)
    },

    async logout ({ commit }) {
      await authAPI.logout()
      commit('setUser', undefined)
    }
  }
}
