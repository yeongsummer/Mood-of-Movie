<template>
  <v-container style="width: 80vw">
    <div id='nav'>
      <span>
        <router-link :to="{ name: 'MovieList' }" class="text-btn">Ranking </router-link> | 
        <router-link :to="{ name: 'MovieRecommend' }" class="text-btn"> Recommend</router-link> |
        <router-link :to="{ name: 'ReviewList' }" class="text-btn"> Review</router-link>
      </span>
    </div>
    <!-- <div class="background" :style="{'background-image': 'url('+require('@/assets/main_image.jpg')+')'}">
      <div class="main_text">
        <p>지금 나에게 맞는 영화를 찾고,</p>
        <p>나만의 영화 경험을 공유하세요.</p>
      </div>
    </div> -->
    <v-toolbar
      id="toolbar"
      color="green darken-1"
      dark
    >

      <v-toolbar-title>Review</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-autocomplete
        v-model="select"
        :loading="loading"
        :items="items"
        :search-input.sync="search"
        cache-items
        class="mx-4"
        flat
        hide-no-data
        hide-details
        label="영화 제목을 검색해주세요 :)"
        solo-inverted
        @keypress.enter="searchMovie(search)"
      ></v-autocomplete>
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
    <h1>{{ movie_title }}</h1>
    <v-list
      two-line
    >
      <template v-for="(review, index) in review_list">
        <v-list-item
          :key="review.id"
        >
          <v-list-item-content>
            <v-rating
              color="yellow darken-3"
              background-color="grey darken-1"
              empty-icon="$ratingFull"
              half-increments
              readonly
              hover
              size="15"
              :value="review.rank/2"
            ></v-rating>
            <v-list-item-title v-text="review.title"></v-list-item-title>
          </v-list-item-content>

          <v-list-item-action>
            <v-btn
              text
              @click="goReviewDetail(review.id)"
            >
              자세히보기
            </v-btn>
          </v-list-item-action>
        </v-list-item>

        <v-divider
          v-if="index < review_list.length - 1"
          :key="index"
        ></v-divider>
      </template>
    </v-list>
  </v-container>
</template>

<script>

import axios from 'axios'
import { mapState } from 'vuex'
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

      loading: false,
      items: [],
      search: null,
      select: null,
      movie_title:null,
    }
  },
  computed: {
    ...mapState([
      'movie_list'
    ])
  },
  watch: {
    search (val) {
      val && val !== this.select && this.querySelections(val)
    },
  },
  methods: {
    setToken: function () {
        const token = localStorage.getItem('jwt')
        const config = {
          Authorization: `JWT ${token}`
        }
        return config
      },
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
    },
    querySelections (v) {
      this.loading = true
      // Simulated ajax query
      setTimeout(() => {
        this.items = this.movie_list.filter(e => {
          return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
        })
        this.loading = false
      }, 500)
    },
    searchMovie(search) {
      this.movie_title = search
      console.log(search)
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/review_search/${search}/`,
        headers: this.setToken(),
        })
        .then(res => {
          this.review_list = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }

  },
  created: function () {
    if (this.$route.params.movie_pk) {
      this.movie_pk = this.$route.params.movie_pk
      this.movie_title = this.$route.params.movie_title
      this.getReview()
    } 
  }
}
</script>

<style scoped>

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

#toolbar {
  margin-bottom: 20px;
}
</style>