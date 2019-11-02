import Vue from 'vue'
import VueRouter from 'vue-router'
import SignIn from '@/views/SignIn.vue'
import Activity from '@/views/Activity.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/activity',
    name: 'Activity',
    component: Activity
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.afterEach(to => {
  localStorage.lastRoute = to.name
})

export default router
