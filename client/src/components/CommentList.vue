<template>
  <div>
    <div v-for="comment in comments" :key="comment.id" class="media mt-3">
      <p style="font-weight:700; margin-bottom:5px;">{{ comment.nickname }}</p>
      <span>{{ comment.content }}</span>
      <span style="margin-left:10px; font-size:12px;">{{ comment.created_at | moment('YYYY-MM-DD') }}</span>
      <v-btn class="ml-4" small depressed v-if="comment.nickname === nickname " @click="deleteComment(comment)">
        삭제
      </v-btn>
      <hr style="margin-top: 5px;">
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
  },
  created() {
    console.log(this.comments)
  }
}

</script>

<style>

</style>