import Vue from 'vue'
import VueRouter from 'vue-router'
import UserSelection from '../views/UserSelection.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'user-selection',
    component: UserSelection
  },
  {
    path: '/item-selection',
    name: 'item-selection',
    component: () => import('../views/ItemSelection.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
