<template>
  <v-container style="width: 80vw;">
    <div class="updatereview_container">
      <div class="row">
        <v-text-field
          color='green darken-1'
          label="리뷰 제목을 입력하세요"
          :rules="rules"
          hide-details="auto"
          v-model.trim="title"
        ></v-text-field>
      </div>
      <div class="row my-5">
        <v-rating
          color="yellow darken-3"
          background-color="grey darken-1"
          empty-icon="$ratingFull"
          half-increments
          hover
          medium
          v-model="rank"
        ></v-rating>
      </div>
      <div class="row my-2">
        <v-textarea
          color='green darken-1'
          label="리뷰 내용을 입력하세요"
          auto-grow
          outlined
          rows="5"
          row-height="40"
          shaped
          v-model.trim="content"
        ></v-textarea>
      </div>
      <div align="right">
        <v-btn @click="goBack()" color='grey lighten-1 mr-5' class="white--text" large>취소</v-btn>
        <v-btn @click="updateReview()" color='green lighten-1 mr-2' class="white--text" large>작성 완료</v-btn>
      </div>
    </div>  
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  name: "CreateReview",
  data: function () {
    return {
      review_pk: null,
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
    goBack: function () {
      this.$router.push({ name: "ReviewDetail", params: { review_pk: this.review_pk }} )
    },
    updateReview: function () {
      const reviewItem = {
        title: this.title,
        content: this.content,
        rank: this.rank*2
      }
      if (reviewItem.content) {
        axios({
          method: 'put',
          url: `http://127.0.0.1:8000/movies/review/${this.review_pk}/`,
          data: reviewItem,
          headers: this.setToken()
          })
          .then(res => {
            console.log(res)
            this.title = null
            this.content = null
            this.rank = null
            this.$router.push({ name: "ReviewDetail", params: { review_pk: this.review_pk }} )
          })
        .catch(err => {
          console.log(err)
        })
      }
    },
  },
  created: function () {
    this.review_pk = this.$route.params.review_pk
    this.title = this.$route.params.title
    this.rank = this.$route.params.rank/2
    this.content = this.$route.params.content
  },
}
</script>

<style>
.updatereview_container {
  margin-top: 3%;
  border: 2px solid #A5D6A7;
  border-radius: 10px;
  padding: 3%;
}
</style>