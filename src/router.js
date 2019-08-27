import Vue from 'vue'
import Router from 'vue-router'
import Questionpage from './views/contest/Questionpage.vue'
import Home from './views/Home.vue'
import Signin from './views/user/Signin.vue'
import Signup from './views/user/Signup.vue'
import Mypage from './views/user/Mypage.vue'
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
