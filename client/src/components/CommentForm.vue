<template>
  <div class="container">
    <b>댓글</b>
    <p>{{comments.count}}</p>
    <v-textarea
      style="width: 100%;"
      id="content"
      auto-grow
      outlined
      rows="2"
      row-height="15"
      v-model="content"
      color='green darken-1'
      @keypress.enter="createComment"
    ></v-textarea>
  </div>
</template>

<script>
  import axios from 'axios'
  import { mapState } from 'vuex'
  export default {
    name: 'CommentForm',
    data: function () {
      return {
        content: '',
      }
    },
    computed: {
    ...mapState([
      'nickname',
      'comments'
      ])
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
            console.log(res.data)
            const commentItem = {
              id: res.data.id,
              nickname: this.nickname,
              content: this.content,
              created_at: res.data.created_at,
            }
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