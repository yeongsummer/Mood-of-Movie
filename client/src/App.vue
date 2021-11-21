<template>
  <v-app>
    <navbar/>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
// import MovieList from "@/views/movies/MovieList.vue"

export default {
  name: 'App',

  components: {
    Navbar,
    // MovieList,
  },

  data: () => ({
    //
  }),
};
</script>
