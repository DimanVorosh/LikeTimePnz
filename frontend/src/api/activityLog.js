import axios from './index'

export default {
  async getActivityLogs (payload) {
    try {
      const activityLogs = await axios.get(`/activity?date=${payload.date}`)
      return activityLogs.data
    } catch (error) {
      return error.response.status
    }
  }
}
