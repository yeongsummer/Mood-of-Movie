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
            <p>작성자: {{reviewUsername}}</p>
            <p>영화: {{movie}}</p>
            <p>작성: {{ review.created_at | moment('YYYY-MM-DD hh:mm') }} | 최근수정:
              {{ review.updated_at | moment('YYYY-MM-DD hh:mm') }} </p>
            <p class="font-2em">
              {{review.content}}
            </p>
            <div class="d-flex justify-content-end">
              <!--작성자와 접속자가 같다면, 수정/삭제 버튼 활성화-->
              <!--단, 관리자의 경우 삭제 버튼 활성화 -->
              <button class="btn btn-warning font-do mr-3 font-1-2em"
                v-if="reviewUsername === this.$store.state.username">글 수정</button>

              <button class="btn btn-danger font-do mr-3 font-1-2em" v-if="this.$store.state.is_admin"
                @click="deletereview(review)">글 삭제</button>
              <button v-else-if="reviewUsername === this.$store.state.username" class="btn btn-danger font-do mr-3 font-1-2em">글 삭제</button>
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
        reviewUsername: '',
        reviewItem: '',
        commentList: [],
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
  //     backToreview: function () {
  //       this.$router.push({
  //         name: 'review'
  //       })
  //     },
  //     deleteReview: function (review) {
  //       const config = this.setToken()
  //       axios.delete(`${SERVER_URL}/community/review_delete_update/${review.id}/`, config)
  //         .then(() => {
  //           this.$router.push({
  //             name: 'review'
  //           })
  //         })
  //         .catch((err) => {
  //           console.log(err)
  //         })
  //     },
  //     updatereviewForm: function (review) {
  //       const reviewItem = {
  //         id: review.id,
  //         purpose: 'update',
  //         title: review.title,
  //         content: review.content
  //       }
  //       this.$router.push({
  //         name: 'Createreview',
  //         params: reviewItem
  //       })
  //       //console.log(review.id)
  //     },
    },
    created: function () {
      this.review_pk = this.$route.params.review_pk
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/review/${this.review_pk}/`,
        headers: this.setToken()
        })
        .then(res => {
          this.review = res.data
          console.log(this.review)
          this.reviewUsername = this.review.user.username
          this.movie = this.review.movie.title
        })
        .catch(err => {
          console.log(err)
        })
      this.getComments()
    },
    mounted() {
      window.scrollTo(0,0)
  }
}
</script>

<style scoped>
</style>