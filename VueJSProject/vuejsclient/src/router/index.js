import { createRouter, createWebHistory } from 'vue-router'

import mainPage from '../views/MainPage.vue'
import cartPage from '../views/cart.vue'
import viewInfo from '../views/viewInfo.vue'
import LoginRegister from '../views/LoginRegister.vue';
import profile from '../views/profile.vue'
import applyMembership from '../views/applyMembership.vue'
import track from '../views/trackStatus.vue'
const routes = [

  {
    path: '/',
    name: 'mainPage',
    component: mainPage
  },
  {
    path: '/cart',
    name: 'cart',
    component: cartPage
  },
  {
    path: '/LoginRegister',
    name: 'LoginRegister',
    component: LoginRegister
  },
  {
    path: '/viewInfo',
    name: 'viewInfo',
    component: viewInfo
  },
  {
    path: '/profile',
    name: 'profile',
    component:profile
    },
    {
      path: '/applyMembership',
      name: 'applyMembership',
      component:applyMembership
      },
      {
        path: '/track',
        name: 'track',
        component: track
      },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
