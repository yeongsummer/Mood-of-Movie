<template>
  <v-container style="width: 80vw;">
    <div class="review_container">
      <div style="font-size:25px; font-weight:700; margin-bottom:30px;">
        {{reviewUsername}}님의 <span style="background-color:#C8E6C9; font-size:30px;">{{ movie_title }}</span> 리뷰
      </div>
      <div>
        <v-row>
          <v-col style="max-width:230px; margin-right: 5px;">
            <v-img
              :src="getImgUrl(movie_poster)"
              :lazy-src="getImgUrl(movie_poster)"
              height="329"
              width="230"
              style="border-radius:7px;"
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
          </v-col>
          <v-col>
            <div class="review_title_box" justify="space-around">
              <span style="font-size:25px; font-weight:700;">{{review.title}}</span>
              <v-rating
                class="d-inline"
                color="yellow darken-3"
                background-color="grey darken-1"
                empty-icon="$ratingFull"
                half-increments
                readonly
                hover
                size="20"
                :value="review.rank/2"
                style="margin-left:10px;"
              ></v-rating>
              <span>{{review.rank}}</span>
              <div style="text-align: left; font-size: 0.9rem;">작성: {{ review.created_at | moment('YYYY-MM-DD') }} | 최근수정:
                {{ review.updated_at | moment('YYYY-MM-DD') }} </div>
            </div>
            <v-btn text @click="goProfile()" class="mb-3">
              {{reviewUsername}}님의 모든 리뷰 더보기 >
            </v-btn>
            <div>
              {{review.content}}
            </div>
            <div align="right">
              <v-btn icon :color="liked? 'pink':'grey'" @click.stop="reviewLike(review.id)">
                <v-icon>mdi-heart</v-icon>
              </v-btn>
              <span style="margin-right:20px;">{{ like_count }}</span>
            </div>
            <br>
            <div align="right" class="">
              <v-btn color='green lighten-1' class="white--text mr-2" depressed v-if="reviewUsername === nickname" @click="updateReview(review)">
                수정
              </v-btn>
              <v-btn color='green lighten-1' class="white--text mr-2" depressed v-if="reviewUsername === nickname" @click="deleteReview(review)">
                삭제
              </v-btn>
              <v-btn color='green lighten-1' class="white--text mr-2" depressed @click="backToReviewList">
                뒤로가기
              </v-btn>
            </div>
          </v-col>
        </v-row>
      </div>
      <br>
      <CommentForm :review="review"/>
      <CommentList :review="review"/>
    </div>
  </v-container>
</template>

<script>
  // const SERVER_URL = process.env.VUE_APP_SERVER_URL
  import axios from 'axios'
  import CommentList from '@/components/CommentList'
  import CommentForm from '@/components/CommentForm'
  import { mapState } from 'vuex'
  export default {
    name: 'ReviewDetail',
    components: {
      CommentList,
      CommentForm,
    },
    data: function () {
      return {
        review_pk: '',
        review: '',
        movie_title: '',
        movie_pk:'',
        reviewUsername: '',
        reviewerEmail: '',
        reviewItem: '',
        commentList: [],
        liked: false,
        like_count: 0,
      }
    },
    computed: {
    ...mapState([
      'nickname',
    ])
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
      getComments: function () {
        console.log('this.review',this.review)
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/comment_list/${this.review_pk}/`,
          headers: this.setToken()
        })
        .then(res => {
          this.$store.dispatch('getComments', res.data)
          console.log(res.data)
          
        })
        .catch(err => {
          console.log(err)
        })
      },
      backToReviewList: function () {
        this.$router.push({name: 'ReviewList', params: {movie_pk: this.movie_pk, movie_title: this.movie_title}})
      },
      deleteReview: function () {
        axios({
          method: 'delete',
          url: `http://127.0.0.1:8000/movies/review/${this.review_pk}/`,
          headers: this.setToken()
          })
          .then(res => {
            console.log(res)
            this.$router.push({name: 'ReviewList', params: {movie_pk: this.movie_pk, movie_title: this.movie_title}})
          })
          .catch((err) => {
            console.log(err)
          })
      },
      updateReview: function (review) {
        const reviewItem = {
          review_pk: review.id,
          title: review.title,
          rank: review.rank,
          content: review.content,
          movie: this.movie
        }
        this.$router.push({name: 'UpdateReview', params: reviewItem})
        //console.log(review.id)
      },
      reviewLike: function (review_pk) {
        this.liked = !this.liked
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/review_like/${review_pk}/`,
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
      goProfile() {
        this.$router.push(`/accounts/${this.reviewUsername}/profile`)
      }
    },
    created: function () {
      console.log('email')
      console.log(this.email)
      this.review_pk = this.$route.params.review_pk

      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/review/${this.review_pk}/`,
        headers: this.setToken()
        })
        .then(res => {
          this.review = res.data
          console.log(this.review)
          this.reviewUsername = this.review.user.nickname
          this.reviewerEmail = this.review.user.email
          this.movie_title = this.review.movie.title
          this.movie_pk = this.review.movie.id
          this.movie_poster = this.review.movie.poster_path
        })
        .catch(err => {
          console.log(err)
        })
      this.getComments()

      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/review_like/${this.review.id}/`,
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
    mounted() {
      window.scrollTo(0,0)
  }
}
</script>

<style scoped>
.review_container {
  margin-top: 3%;
  margin-bottom: 3%;
  border: 2px solid #8FBC8B;
  border-radius: 10px;
  padding: 3%;
}

.review_title_box {
  background-color: #EFE8D8;
  padding: 15px 20px 15px 20px;
  border-radius: 10px;
}
</style>