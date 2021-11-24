<template>
  <div style="width: 100%;">
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
      <div>
        <v-btn icon :color="liked? 'pink':'grey'" @click.stop="movieLike(movie.id)">
          <v-icon>mdi-heart</v-icon>
        </v-btn>
        <span>{{ like_count }}</span>
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
        <v-card-text style="padding-bottom:15px;">
          <span class="text-h4 font-weight-bold" style="color:#484848;">{{ movie.title }}</span>
        </v-card-text>
        <v-card-text>
          <div class="detail">
            개봉일: {{ movie.release_date | moment('YYYY-MM-DD') }}
          </div>
          <div class="detail">
            장르:
            <span v-for="(genre, index) in genres" :key=index style="margin: 2px;">
              {{genre}}
            </span>
          </div>
          <div class="director">
            <span v-for="(director,index) in directors" :key=index> 
              감독: {{ director }}
            </span>
          </div>
        </v-card-text>
        <v-card-text style="margin-bottom: 10px;">
          <div>
            <div id="tmdb" style="font-size:20px; font-weight: 700; ">
              TMDB
            </div>
            <span  style="font-size:20px; font-weight: 700; color: #484848; margin-left: 5px;">{{ movie.vote_average }}</span> / 10
          </div>
        </v-card-text>
        <v-card-text style="padding-bottom:10px;">
          <div style="color: #484848;">
            {{ movie.overview }}
          </div>
        </v-card-text>
        <v-spacer></v-spacer>
        <v-card-actions>
          <div align="right">
            <v-btn
              v-if="isLogin"
              color='green lighten-1' 
              class="white--text mr-2" 
              depressed
              @click="goReview(movie.id, movie.title)"
            >
              리뷰보러가기
            </v-btn>
          </div>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
export default {
  name: "RecommendItem",
  props: {
    movie:Object
  },
  data: function() {
    return {
      dialog: false,
      movie_director: '',
      videoId:'',
      directors: [],
      genres: [],
      liked: false,
      like_count: 0,
      review_list: [],
    }
  },
  computed: {
    ...mapState([
      'isLogin'
    ]),
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
          this.genres = res.data.genre_list
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
}
</script>

<style>
.detail {
  background-color:#EFE8D8;
  display: inline;
  border-radius: 5px;
  margin: 5px;
  padding: 6px;
  font-weight: 600;
  color: #484848;
}

.director {
  background-color:#C8E6C9;
  display: inline;
  border-radius: 5px;
  margin: 5px;
  padding: 6px;
  font-weight: 600;
  color: #484848;
}

#tmdb {
  font-size:20px; 
  font-weight: 700;
  background-color:#150e68;
  color: white;
  display: inline;
  border-radius: 4px;
  margin: 5px;
  padding: 3px 4px 5px 7px;
}
</style>