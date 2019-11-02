import activityLogAPI from '@/api/activityLog'

export default {

  state: {
    logs: undefined
  },

  mutations: {
    setActivityLogs (state, activityLogs) {
      state.logs = activityLogs
    }
  },

  actions: {
    async getActivityLogs ({ commit }, date) {
      const activityLogs = await activityLogAPI.getActivityLogs(date)
      commit('setActivityLogs', activityLogs)
    }
  }
}
