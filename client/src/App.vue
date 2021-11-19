<template>
  <div id='app'>
    <movieList/>
  </div>
</template>

<script>
import MovieList from "@/views/movies/MovieList.vue";
export default {
  name: 'App',
  components: {
    MovieList,
  }
}
</script>
