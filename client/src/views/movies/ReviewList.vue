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
    <v-toolbar
      color="cyan"
      dark
    >

      <v-toolbar-title>Review</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn
        icon
        @click="goCreateReview(movie.id)"
      >
        <v-icon dark>
          mdi-pencil
        </v-icon>
      </v-btn>
    </v-toolbar>

    <div v-for="review in review_list" :key="review.id">
      <p>{{review.title}}</p>
      <v-rating
        color="yellow darken-3"
        background-color="grey darken-1"
        empty-icon="$ratingFull"
        half-increments
        readonly
        hover
        size="15"
        :value="review.rank"
      ></v-rating>
      <v-btn
        text
        @click="goReviewDetail(review.id)"
      >
        자세히보기
      </v-btn>
      <br>
    </div>
  </v-container>
</template>

<script>

import axios from 'axios'
// import _ from 'lodash'

export default {
  name: 'ReviewList',
  components: {
  },
  data: function () {
    return {
      movie_pk: '',
      movies: {
        type: Array,
        required: true
      },
      review_list: [],
    }
  },
  methods: {
    getReview: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/review_list/${this.movie_pk}/`,
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
  created: function () {
    if (this.$route.params.movie_pk) {
      this.movie_pk = this.$route.params.movie_pk
      this.getReview()
    }
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