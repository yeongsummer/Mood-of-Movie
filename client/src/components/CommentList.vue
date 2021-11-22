<template>
  <div>
    <h3>댓글 목록</h3>

    <div v-for="comment in comments" :key="comment.id" class="media mt-3">
      <!-- <h3>{{ comment.user.nickname }}</h3> -->
      <p>{{ comment.content }}</p>
    </div>
  </div>
</template>

<script>
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
      'login',
      'login_user',
      'nickname',
      'comments',
    ])
  },

    
}
</script>

<style>

</style>