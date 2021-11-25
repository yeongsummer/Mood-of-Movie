<template>
<div style="width: 100%; margin-right:55px;">
  <v-card
    class="ma-4"
    width="14.5vw"
    @click="[getMovieVideoKey(movie.id), dialog = true]"
  >
    <div>
      <v-img
        :src="getImgUrl(movie.poster_path)"
        :lazy-src="getImgUrl(movie.poster_path)"
        style="height:22vw;"
      >
        <template v-slot:placeholder>
          <v-row class="fill-height ma-0" align="center" justify="center">
            <v-progress-circular
              indeterminate
              color="grey lighten-5"
            ></v-progress-circular>
          </v-row>
        </template>
      </v-img>
    </div>
  </v-card>
  <v-dialog
      v-model="dialog"
      width="700"
    >
      <v-card>
        <div class="video-container pa-4" align="center" style="height: 100%;">
          <iframe 
            class="video-iframe"
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen
            :src="thumbnailUrl"
            width="100%"
            height="400px;"
          >
          </iframe>
        </div>
        <v-card-title>
          <span class="text-h5">{{ movie.title }}</span>
        </v-card-title>
        <template >
          <v-card-text v-for="(director,index) in directors" :key=index>
            <p>{{ director }}</p>
            <p>{{ movie.vote_average }} / 10</p>
            <div>
              {{ movie.overview }}
            </div>
          </v-card-text>
        </template>
        <v-spacer></v-spacer>
        <v-card-actions>
          <v-btn
            text
            color="teal accent-4"
            @click="goReview(movie.id)"
          >
            리뷰보러가기
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "LikeMovieItem",
  props: {
    movie: Object,
  },
  data: function () {
    return {
      dialog: false,
      movie_director: '',
      videoId:'',
      directors: [],
      liked: false,
      like_count: 0,
      review_list: [],
    }
  },
  computed: {
    thumbnailUrl() {
      return `https://www.youtube.com/embed/${this.videoId}?autoplay=1&mute=1`
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getImgUrl: function (url) {
      const imgUrl = `https://image.tmdb.org/t/p/w300/${url}`
      return imgUrl
    },
    getMovieVideoKey: function (movie_pk) {
      console.log(movie_pk)
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/movie_video/${movie_pk}/`,
        })
        .then(res => {
          this.videoId = res.data.video_key
          this.directors = res.data.director_list
        })
        .catch(err => {
          console.log(err)
        })
    },
    movieLike: function (movie_pk) {
      this.liked = !this.liked
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/movie_like/${movie_pk}/`,
        headers: this.setToken()
        })
        .then(res => {
          console.log(res)
          this.like_count = res.data.like_count
          console.log(this.like_count)
        })
        .catch(err => {
          console.log(err)
        })
    },
    goReview(movie_pk) {
      this.$router.push({ name: "ReviewList", params: { movie_pk: movie_pk }} )
    },
  },
}
</script>

<style>

</style>