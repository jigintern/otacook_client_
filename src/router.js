import Vue from 'vue'
import Router from 'vue-router'
import Questionpage from './views/Questionpage.vue'
import Home from './views/Home.vue'
import Signin from './views/Signin.vue'
import Signup from './views/Signup.vue'
import Mypage from './views/Mypage.vue'
import app from './App.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/signin',
      name: 'Signin',
      component: Signin
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup
    },
    {
      path: '/mypage',
      name: 'Mypgae',
      component: Mypage
    },
    {
      path: '/questionpage',
      name: 'Questionpage',
      component: Questionpage
    },
  ]
})
