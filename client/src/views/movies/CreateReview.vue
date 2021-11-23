<template>
  <v-container>
    <div class="row my-2">
      <v-text-field
        label="리뷰 제목을 입력하세요"
        :rules="rules"
        hide-details="auto"
        v-model.trim="title"
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
        ></v-textarea>
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
        rank: this.rank*2
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
            this.$router.push({ name: "ReviewDetail", params: { review_pk: res.data.id }} )
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