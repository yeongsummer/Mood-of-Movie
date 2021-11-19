<template>
  <v-app>
    <app-navbar/>
    <movieList/>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import MovieList from "@/views/movies/MovieList.vue";

export default {
  name: 'App',

  components: {
    appNavbar: Navbar,
    MovieList,
  },

  data: () => ({
    //
  }),
};
</script>
