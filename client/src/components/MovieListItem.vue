<template>
  <v-dialog
    width="700px"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-col md="3">
        <v-card 
          class="mx-auto mb-10"
          max-width="200" 
          v-bind="attrs"
          v-on="on"
          @click="getMovieVideoKey(movie.id)"
        >
          <v-img
            :src="getImgUrl(movie.poster_path)"
            :lazy-src="getImgUrl(movie.poster_path)"
            max-height="290"
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
          <!-- <v-card-text class="fw-bold text-start text-nowrap overflow-hidden">
            {{ movie.title }}
          </v-card-text> -->
          <v-card-actions @click="likeBtn(movie.id)">
            <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn>
            <!-- <v-spacer></v-spacer> -->
            <span>256</span>
          </v-card-actions>
        </v-card>
      </v-col>
    </template>
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
      <template  v-if="!reveal">
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
          @click="[reveal = true, getReview(movie.id)]"
          v-if="!reveal"
        >
          리뷰보러가기
        </v-btn>
      </v-card-actions>

      <v-expand-transition>
        <v-card
          v-if="reveal"
          class="transition-fast-in-fast-out v-card--reveal"
          style="height: 100%;"
        >
          <v-toolbar
            color="cyan"
            dark
          >

            <v-toolbar-title>Review</v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn
              icon
              @click="goCreateReview(movie.id)"
            >
              <v-icon dark>
                mdi-pencil
              </v-icon>
            </v-btn>
          </v-toolbar>
          <v-list three-line>
            <template v-for="(review, index) in review_list">
              <v-list-item :key="review.pk">
                <v-list-item-content>
                  <v-list-item-title v-text="review.title"></v-list-item-title>
                  <v-list-item-rank v-text="review.rank"></v-list-item-rank>
                </v-list-item-content>
              </v-list-item>

              <v-divider
                v-if="review < reviews.length - 1"
                :key="index"
              ></v-divider>
            </template>
          </v-list>
            



          <!-- <div v-for="review in review_list" :key="review.id">
            <span>{{ review.title }}</span>
            <span>평점: {{ review.rank }}</span>
            <v-btn
              text
              @click="goReviewDetail(review.id)"
            >
              자세히보기
            </v-btn>
          </div> -->
          <v-card-actions class="pt-0">
            <v-btn
              text
              color="teal accent-4"
              @click="reveal = false"
            >
              Close
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-expand-transition>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieListItem',
  data: function() {
    return {
      reveal: false,
      movie_director: '',
      videoId:'',
      directors: [],
      liked: false,
      like_count: 0,
      review_list: [],
    }
  },
  props: {
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
          console.log(res)
          this.videoId = res.data.video_key
          this.directors = res.data.director_list
        })
        .catch(err => {
          console.log(err)
        })
    },
    likeBtn: function (movie_pk) {
      this.liked = !this.liked
      this.like_count += 1
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/movie_like/${movie_pk}/`,
        })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getReview: function (movie_pk) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/review_list/${movie_pk}/`,
        })
        .then(res => {
          this.review_list = res.data
          console.log('getReview',res)
        })
        .catch(err => {
          console.log(err)
        })
    },
    goReviewDetail: function (review_pk) {
      this.$router.push({ name: "ReviewDetail", params: { review_pk: review_pk }})
    },
    goCreateReview: function (movie_pk) {
      this.$router.push({ name: "CreateReview", params: { movie_pk: movie_pk }})
    }
  },
  // created() {
  //   axios({
  //     method: 'get',
  //     url: `http://127.0.0.1:8000/movies/movie_like/${this.movie.pk}/`,
  //     })
  //     .then(res => {
  //       this.like_count = res
  //       console.log(res)
  //     })
  //     .catch(err => {
  //       console.log(err)
  //     })
  // }
}
</script>

<style>
.v-card--reveal {
  bottom: 0;
  opacity: 1 !important;
  position: absolute;
  width: 100%;
}
</style>