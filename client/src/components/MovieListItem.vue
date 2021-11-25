<template>
  <v-col md="4">
    <div>
      <v-row>
        <v-col style="max-width:110px; position: relative;">
          <span class="ranking" style="text-shadow:4px 5px #f1cb70">{{ index+1 }}</span>
        </v-col>
        <v-col>
          <v-card 
            style="width:15vw; margin-top:30px; margin-bottom:30px;"
            @click="[getMovieVideoKey(movie.id), dialog = true]"
          >
            <v-img
              :src="getImgUrl(movie.poster_path)"
              :lazy-src="getImgUrl(movie.poster_path)"
              style="height:45vh;"
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
            <v-btn icon :color="liked? 'pink':'grey'" @click.stop="movieLike(movie.id)">
              <v-icon>mdi-heart</v-icon>
            </v-btn>
            <!-- <v-spacer></v-spacer> -->
            <span>{{ like_count }}</span>
          </v-card>
        </v-col>
      </v-row>
    </div>
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
          <span class="text-h5 font-weight-bold" style="background-color:#C8E6C9;">{{ movie.title }}</span>
        </v-card-title>
        <template >
          <v-card-text v-for="(director,index) in directors" :key=index>
            <p>감독: {{ director }}</p>
            <p>평점: {{ movie.vote_average }} / 10</p>
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
            @click="goReview(movie.id, movie.title)"
          >
            리뷰보러가기
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-col>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieListItem',
  data: function() {
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
  props: {
    index:Number,
    movie: {
      type: Object,
      required: true
    },
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
        headers: this.setToken()
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
    goReview(movie_pk, movie_title) {
      this.$router.push({ name: "ReviewList", params: { movie_pk: movie_pk, movie_title: movie_title }} )
    },
  },
  created() {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/movie_like/${this.movie.id}/`,
      headers: this.setToken()
      })
      .then(res => {
        console.log(res)
        this.like_count = res.data.like_count
        this.liked = res.data.liked
      })
      .catch(err => {
        console.log(err)
      })
  },
}
</script>

<style scoped>
.ranking {
  position: absolute;
  right: 0;
  top: 30px;
  margin-left: 10px;
  font-size: 4.5rem;
  font-weight: 700;
  color: rgb(61, 53, 7);
}
</style>