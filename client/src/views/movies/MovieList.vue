<template>
  <v-container>
    <div id='nav'>
      <span>
        <router-link :to="{ name: 'MovieList' }" class="text-btn">Ranking </router-link> | 
        <router-link :to="{ name: 'MovieRecommend' }" class="text-btn"> Recommend</router-link> |
        <router-link :to="{ name: 'ReviewList' }" class="text-btn"> Review</router-link>
      </span>
    </div>
    <div class="background" :style="{'background-image': 'url('+require('@/assets/main_image.jpg')+')'}">
      <div class="main_text">
        <p>지금 나에게 맞는 영화를 찾고,</p>
        <p>나만의 영화 경험을 공유하세요.</p>
      </div>
    </div>
    <h1 class="text-center" style="margin: 20px;">TOP 20</h1>
    <v-row no-gutters class="justify-center background" :style="{'background-image': 'url('+require('@/assets/list_cover.png')+')'}">
      <movie-list-item 
        v-for="movie in movies" 
        :key="movie.id"
        :movie="movie"
      >
      </movie-list-item>
    </v-row>
  </v-container>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'

import axios from 'axios'
// import _ from 'lodash'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  data: function () {
    return {
      movies: {
        type: Array,
        required: true
      }
    }
  },
  methods: {
    getMovies: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/',
        })
        .then(res => {
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created: function () {
    this.getMovies()
  }
}
</script>

<style>
#nav {
  text-align: center;
  padding: 20px;
}

#nav a {
  font-weight: 500;
  font-size: 20px;
  color: #2c3e50;
  text-decoration: none;
}

#nav a.router-link-exact-active {
  font-size: 30px;
  color: #42b983;
}

.background {
  background-size: 100% 100%;
}

.main_text{
  margin-left: 50px;
  padding-top: 20%;
  padding-bottom: 15%;
  color: white;
  font-size: 2.5vw;
  font-weight: 700;
}
</style>