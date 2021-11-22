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
        v-for="movie in recommended_movies" 
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

export default {
  name: 'MovieRecommend',
  components: {
    MovieListItem,
  },
    data: function () {
      return {
        movie_title: '',
        recommended_movies: {
          type: Array,
          required: true
        }
      }
  },
  methods: {
    getRecommendedMovies: function (movie_title) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/movie_recommend',
        params: movie_title,
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
    this.getRecommendedMovies(this.movie_title)
  }
}
</script>

<style>

</style>