import Vue from 'vue'
import Router from 'vue-router'
import Questionpage from './views/Questionpage.vue'
import Home from './views/Home.vue'
import app from './App.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Questionpage',
      component: Questionpage
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    }
  ]
})
