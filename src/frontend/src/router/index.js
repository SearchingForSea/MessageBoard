import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserLogin from '../views/UserLogin.vue'
import UserRegister from '../views/UserRegister.vue'

Vue.use(VueRouter)

// const originalPush = VueRouter.prototype.push
// VueRouter.prototype.push = function push (location) {
//   return originalPush.call(this, location).catch(err => err)
// }

const routes = [
  {
    path: '/',
    name: 'user',
    component: UserLogin
  },
  {
    path: '/home/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: UserLogin
  },
  {
    path: '/register',
    name: 'register',
    component: UserRegister
  }
]

const router = new VueRouter({
  routes
})

export default router
