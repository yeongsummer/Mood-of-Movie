import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '../views/accounts/Signup.vue'
import Login from '../views/accounts/Login.vue'
import MovieList from '../views/movies/MovieList.vue'
import Password from '../views/accounts/Password.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/password',
    name: 'Password',
    component: Password,
  },
  {
    path: '/movies',
    name: 'MovieList',
    component: MovieList,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
