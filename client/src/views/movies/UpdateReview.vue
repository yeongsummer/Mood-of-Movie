<template>
  <v-container>
    <h2>리뷰 수정하기</h2>
    <div class="row my-2">
      <v-text-field
        label="리뷰 제목을 입력하세요"
        :rules="rules"
        hide-details="auto"
        v-model.trim="title"
        :value="title"
      ></v-text-field>
    </div>
    <div class="row my-2">
      <v-rating
        color="yellow darken-3"
        background-color="grey darken-1"
        empty-icon="$ratingFull"
        half-increments
        hover
        large
        v-model="rank"
        :value="rank"
      ></v-rating>
    </div>
    <div class="row my-2">
        <v-textarea
          label="리뷰 내용을 입력하세요"
          auto-grow
          outlined
          rows="5"
          row-height="50"
          shaped
          v-model.trim="content"
          :value="content"
        ></v-textarea>
    </div>
    <button type="button" class="btn" @click="updateReview()">작성 완료</button>
  
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
    this.rank = this.$route.params.rank
    this.content = this.$route.params.content
  },
}
</script>

<style>
</style>