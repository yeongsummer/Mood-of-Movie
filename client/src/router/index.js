import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '../views/accounts/Signup.vue'
import Login from '../views/accounts/Login.vue'
import Password from '../views/accounts/Password.vue'
import Profile from '../views/accounts/Profile.vue'
import MovieList from '../views/movies/MovieList.vue'
import MovieRecommend from '../views/movies/MovieRecommend.vue'
import ReviewList from '../views/movies/ReviewList.vue'
import CreateReview from '../views/movies/CreateReview.vue'
import ReviewDetail from '../views/movies/ReviewDetail.vue'


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
    path: '/accounts/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/movies',
    name: 'MovieList',
    component: MovieList,
  },
  {
    path: '/movies/movie_recommend',
    name: 'MovieRecommend',
    component: MovieRecommend,
  },
  {
    path: '/movies/review',
    name: 'ReviewList',
    component: ReviewList,
  },
  {
    path: '/movies/createreview',
    name: 'CreateReview',
    component: CreateReview,
  },
  {
    path: '/movies/reviewdetail',
    name: 'ReviewDetail',
    component: ReviewDetail,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
