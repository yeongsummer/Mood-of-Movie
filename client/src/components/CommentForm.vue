<template>
  <div class="container">
    <form v-on:submit.prevent="createComment">
      <div class="row">
        <p>댓글</p>
        <v-textarea
          id="content"
          label="댓글 달기"
          auto-grow
          outlined
          rows="2"
          row-height="15"
          v-model="content"
        ></v-textarea>
        <div class="col-4 d-flex align-items-center">
          <button type="submit" class="btn btn-pink font-1-2em">등록</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'CommentForm',
    data: function () {
      return {
        content: '',
      }
    },
    props: {
      review: {
        type:Object
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
      createComment: function () {
        const commentItem = {
          content: this.content
        }
        const reviewId = this.review.id
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/comment_list/${reviewId}/`,
          data: commentItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            this.$store.dispatch('createComments', commentItem) 
            this.content = ''
          })
          .catch(err => {
            console.log(err)
          })
      },
    },
  }
</script>

<style>
</style>