import Vue from 'vue'
import VueRouter from 'vue-router'
import Password from '../views/accounts/Password.vue'
import Profile from '../views/accounts/Profile.vue'
import MovieList from '../views/movies/MovieList.vue'
import MovieRecommend from '../views/movies/MovieRecommend.vue'
import ReviewList from '../views/movies/ReviewList.vue'
import CreateReview from '../views/movies/CreateReview.vue'
import ReviewDetail from '../views/movies/ReviewDetail.vue'
import UpdateReview from '../views/movies/UpdateReview.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/password',
    name: 'Password',
    component: Password,
  },
  {
    path: '/accounts/:nickname/profile',
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
  {
    path: '/movies/updatereview',
    name: 'UpdateReview',
    component: UpdateReview,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
