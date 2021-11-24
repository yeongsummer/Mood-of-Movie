<template>
  <v-app>
    <navbar/>
    <v-tabs
      id="nav"
      color="basil"
      grow
      v-model="active_tab"
    >
      <v-tabs-slider color="green lighten-1"></v-tabs-slider>
      <v-tab
        v-for="tab of tabs"
        :key="tab.id"
        :to="tab.route"
      >
        {{ tab.name }}
      </v-tab>
      <v-tab-item v-for="tab of tabs" :key="tab.id" :value="tab.route" style="margin-top:40px; width:100%;">
        <router-view></router-view>
      </v-tab-item>
    </v-tabs>

    <!-- <v-main style="padding-top: 0px;">
      <router-view/>
    </v-main> -->
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'App',
  data: function () {
    return {
      // active_tab: '/movies',
      tabs: [
        {id:1, name: 'Ranking', route: '/movies'},
        {id:2, name: 'Recommend & Search', route: '/movies/movie_recommend'},
        {id:3, name: 'Review', route: '/movies/review'}
      ]

    }
  },

  components: {
    Navbar,
  },
  methods: {
    goMovieList() {
      this.$router.push({ name: 'MovieList' })
    },
    goMovieRecommend() {
      this.$router.push({ name: 'MovieRecommend' })
    },
    goReview() {
      this.$router.push({ name: 'ReviewList' })
    }
  }
}
</script>

<style>
#nav {
  margin-top: 50px;
}
#nav a {
  font-weight: 500;
  font-size: 20px;
  color: #324632;
  text-decoration: none;
}
#nav a.router-link-exact-active {
  font-size: 30px;
  color:#66BB6A
}

</style>