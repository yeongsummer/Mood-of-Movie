<template>
  <div>
    <h1>{{ nickname }}님의 마이페이지</h1>
    <v-btn text @click="moveToLink({ name: 'Password' })">Password</v-btn>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { mapActions } from 'vuex'

export default {
  name: 'Profile',
  methods: {
    ...mapActions(['moveToLink']),
  },
  computed: {
    ...mapState([
      'nickname'
    ])
  },
}
</script>

<style>

</style>