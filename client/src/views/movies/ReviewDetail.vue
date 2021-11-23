<template>
  <div>
    <div class="container">
      <div class="row">
        <h1 class="font-do my-5">글 상세보기</h1>
      </div>
      <div class="row d-flex font-poor">
        <div class="media" style="width: 100%; word-break:break-all;">
          <div class="media-body text-justify">
            <h2 class="mt-0">제목: {{review.title}}</h2>
            <p>작성자 : {{reviewUsername}}</p>
            <p>영화: {{movie}}</p>
            <p>작성: {{ review.created_at | moment('YYYY-MM-DD hh:mm') }} | 최근수정:
              {{ review.updated_at | moment('YYYY-MM-DD hh:mm') }} </p>
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
            <p class="font-2em">
              {{review.content}}
            </p>
            <v-btn icon :color="liked? 'pink':'grey'" @click.stop="reviewLike(review.id)">
              <v-icon>mdi-heart</v-icon>
            </v-btn>
            <span>{{ like_count }}</span>

            <div class="d-flex justify-content-end">
              <v-btn depressed v-if="reviewUsername === nickname" @click="updateReview(review)">
                수정
              </v-btn>
              <v-btn depressed v-if="reviewUsername === nickname" @click="deleteReview(review)">
                삭제
              </v-btn>
              <v-btn depressed v-if="reviewUsername === nickname" @click="backToReviewList">
                뒤로가기
              </v-btn>

            </div>
            <div class="mt-5">
              <CommentForm :review="review"/>
              <!-- <CommentForm v-if="this.$store.state.login" :review="review" /> -->
              <!-- <p v-else>댓글을 작성하려면 로그인이 필요합니다. </p> -->
            </div>
            <br>
            <hr>
            <CommentList :review="review"/>
          </div>
        </div>
      </div>
    </div>
  </div>
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
        movie: '',
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
        this.$router.push({name: 'ReviewList', params: {movie_pk: this.movie_pk}})
      },
      deleteReview: function () {
        axios({
          method: 'delete',
          url: `http://127.0.0.1:8000/movies/review/${this.review_pk}/`,
          headers: this.setToken()
          })
          .then(res => {
            console.log(res)
            this.$router.push({name: 'ReviewList', params: {movie_pk: this.movie_pk}})
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
          this.movie = this.review.movie.title
          this.movie_pk = this. review.movie.id
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
</style>