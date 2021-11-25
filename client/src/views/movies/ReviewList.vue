<template>
  <v-container style="width: 80vw">
    <v-toolbar
      id="toolbar"
      dark
      color="green lighten-1"
    >
      <v-toolbar-title>Review</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-autocomplete
        v-if="nickname"
        v-model="select"
        :loading="loading"
        :items="items"
        :search-input.sync="search"
        cache-items
        class="mx-4"
        flat
        hide-no-data
        hide-details
        color='green darken-1'
        label="영화 제목을 검색해주세요 :)"
        solo-inverted
        @keypress.enter="searchMovie(search)"
      ></v-autocomplete>
      <v-spacer></v-spacer>
      <v-btn
        v-if="nickname"
        icon
        @click="goCreateReview()"
      >
        <v-icon dark>
          mdi-pencil
        </v-icon>
      </v-btn>
    </v-toolbar>
    <h1 v-if="!nickname" class="text-center">로그인을 해주세요!</h1>
    <div v-if="nickname" class= "my-10 mx-5 text-center">
      <span style="text-shadow:3px 4px #aed3aa; font-size:40px; font-weight: 700;">{{ movie_title }}</span>
    </div>
    <div v-if="review_list.length == 0" class="text-center">
      <div v-if="flag">
        <div v-if="movie_title">
          <h1>리뷰가 아직 없어요!</h1>
        </div>
      </div>
    </div>
    <review-list-item
      v-for="review in review_list" 
      :key="review.id"
      :review="review"
      @click.native="goReviewDetail(review.id)"
    />
  </v-container>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem'
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'ReviewList',
  components: {
    ReviewListItem
  },
  data: function () {
    return {
      flag: false,
      movie_pk: '',
      movies: {
        type: Array,
        required: true
      },
      review_list: [],

      loading: false,
      items: [],
      search: '',
      select: null,
      movie_title:null,
    }
  },
  computed: {
    ...mapState([
      'movie_list',
      'nickname',
      'isLogin'
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
        headers: this.setToken()
        })
        .then(res => {
          this.review_list = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    goReviewDetail: function (review_pk) {
      this.$router.push({ name: "ReviewDetail", params: { review_pk: review_pk }})
    },
    goCreateReview: function () {
      this.$router.push({ name: "CreateReview", params: { movie_pk: this.movie_pk, movie_title: this.movie_title }})
    },
    querySelections (v) {
      this.loading = true
      setTimeout(() => {
        this.items = this.movie_list.filter(e => {
          return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
        })
        this.loading = false
      }, 500)
    },
    searchMovie(search) {
      this.movie_title = search
      this.flag = true

      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/movie_detail/${search}/`,
        headers: this.setToken(),
        })
        .then(res => {
          console.log('요기!!',res.data)
          this.movie_pk = res.data.id
        })
        .catch(err => {
          console.log(err)
        })

      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/review_search/${search}/`,
        headers: this.setToken(),
        })
        .then(res => {
          this.review_list = res.data
          console.log(this.review_list)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function () {
    if ((this.isLogin) && (this.$route.params.movie_pk)) {
      this.flag = true
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