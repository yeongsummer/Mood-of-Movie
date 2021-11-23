<template>
  <div>
    <h3>댓글 목록</h3>

    <div v-for="comment in comments" :key="comment.id" class="media mt-3">
      <p>{{ comment.nickname }}</p>
      <p>{{ comment.content }}</p>
      <v-btn depressed v-if="comment.nickname === nickname " @click="deleteComment(comment)">
        삭제
      </v-btn>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
export default {
  name: 'CommentList',
  props: {
    review: {
      type:Object
    }
  },
  computed: {
    ...mapState([
      'nickname',
      'login',
      'login_user',
      'email',
      'comments',
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
    deleteComment: function (comment) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/comment/${comment.id}/`,
        headers: this.setToken()
        })
        .then(res => {
          console.log(res)
          this.$store.dispatch('deleteComments', comment)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}

</script>

<style>

</style>