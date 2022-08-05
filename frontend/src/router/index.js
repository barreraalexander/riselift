import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '@/views/LandingView.vue'



const routes = [
  {
    path: '/',
    name: 'landing',
    component: LandingView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '@/views/AboutView.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import(/* webpackChunkName: "about" */ '@/views/LoginView.vue')
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import(/* webpackChunkName: "about" */ '@/views/DashboardView.vue')
  },
  {
    path: '/new_session',
    name: 'new_session',
    component: () => import(/* webpackChunkName: "about" */ '@/views/NewSessionView.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
