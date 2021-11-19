<template>
  <v-container>
    <movie-list-item 
      v-for="movie in movies" 
      :key="movie.id"
      :movie="movie"
      @select-movie="onSelectMovie"
    >
    </movie-list-item>
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

    toDetail: function (movie) {
      this.$router.push({name: 'MovieDetail', query: {movie: movie}})
    },
    onSelectMovie: function (video) {
      this.$emit('select-video', video)
    },
  },
  created: function () {
    this.getMovies()
  }
}
</script>

<style>

</style>