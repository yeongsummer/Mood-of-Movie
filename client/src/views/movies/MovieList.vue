<template>
  <v-container>
    <div id="nav">
      <span>
        <router-link :to="{ name: 'MovieList' }" class="text-btn">Ranking</router-link> | 
        <router-link :to="{ name: 'MovieRecommend' }" class="text-btn">Recommend</router-link>
      </span>
    </div>
    <h1 class="text-center" style="margin-bottom: 20px;">TOP 20</h1>
    <v-row no-gutters class="justify-center">
      <movie-list-item 
        v-for="movie in movies" 
        :key="movie.id"
        :movie="movie"
        @select-movie="onSelectMovie"
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
          console.log(res)
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

</style>