<template>
  <v-container>
    {{ $route.params.movie_pk }}
    <div class="row my-2">
      <input type="text" v-model.trim="title" placeholder="리뷰 제목을 입력하세요">
    </div>
    <div class="row my-2">
      <input type="text" v-model.trim="rank" @keyup.enter="createReview" placeholder="1부터 10까지 평점을 입력하세요">
    </div>
    <div class="row my-2">
        <textarea rows="4" v-model.trim="content" placeholder="리뷰 내용을 입력하세요">
        </textarea>
    </div>
    <button type="button" class="btn" @click="createReview()">작성 완료</button>
  
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  name: "CreateReview",
  data: function () {
    return {
      title: null,
      content: null,
      rank: null,
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
    createReview: function () {
      const reviewItem = {
        title: this.title,
        content: this.content,
        rank: this.rank
      }
      if (reviewItem.content) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/review_list/${this.$route.params.movie_pk}/`,
          data: reviewItem,
          headers: this.setToken()
          })
          .then(res => {
            console.log(res)
            this.title = null
            this.content = null
            this.rank = null
            this.$router.push({ name: "ReviewDetail", query: { review_pk: res.data.review_pk }} )
          })
        .catch(err => {
          console.log(err)
        })
      }
    },
  },
  
}
</script>

<style>
</style>