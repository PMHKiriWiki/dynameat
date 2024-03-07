import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/asteroids',
    name: 'asteroids',
    component: () => import('../views/AsteroidsView.vue')
  },
  {
    path: '/sightings',
    name: 'sightings',
    component: () => import('../views/SightingsView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
