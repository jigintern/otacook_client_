import Vue from 'vue'
import Router from 'vue-router'
import Questionpage from './views/contest/Questionpage.vue'
import Answerpage from './views/contest/Answerpage.vue'
import Rankingpage from './views/contest/Rankingpage.vue'
import Votepage from './views/contest/Votepage.vue'
import Recipepage from './views/default/Recipepage.vue'
import Recipepostpage from './views/default/Recipepostpage.vue'
import Tutorialtoppage from './views/tutorial/Tutorialtoppage.vue'
import Top from './views/default/Top.vue'
import Signin from './views/user/Signin.vue'
import Signup from './views/user/Signup.vue'
import Mypage from './views/user/Mypage.vue'
import app from './App.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Top',
      component: Top
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
    {
      path: '/answerpage',
      name: 'Answerpage',
      component: Answerpage
    },
    {
      path: '/votepage',
      name: 'Voterpage',
      component: Votepage
    },
    {
      path: '/rankingpage',
      name: 'Rankingpage',
      component: Rankingpage
    },
    {
      path: '/recipepage',
      name: 'Recipepage',
      component: Recipepage
    },
    {
      path: '/recipepostpage',
      name: 'Recipepostpage',
      component: Recipepostpage
    },
    {
      path: '/tutorialtoppage',
      name: 'Tutorialtoppage',
      component: Tutorialtoppage
    },
  ]
})
