<template>
  <div>
    <h1>movie list</h1>
    <ul>
      <li v-for="movie in movies" :key="movie.id">
        <img :src="getImgUrl(movie.poster_path)" alt="">
        <span>{{ movie.title }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'

export default {
  name: 'MovieList',
  components: {
    },
  data: function () {
    return {
      movies: [],
    }
  },
  computed: {
    rows() {
      return this.movies.length
    },
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
    getImgUrl: function (url) {
      const imgUrl = `https://image.tmdb.org/t/p/w300/${url}`
      return imgUrl
    },

    // toDetail: function (movie) {
    //   this.$router.push({name: 'MovieDetail', query: {movie: movie}})
    //   // this.$router.push({name: 'MovieDetail', params: {movie: `${movie}`}})
    // }
  },
  created: function () {
    this.getMovies()
  }
}
</script>

<style>

</style>