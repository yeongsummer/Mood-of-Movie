<template>
  <div @click="selectMovie">
    <v-card class="mx-auto" max-width="200">
      <v-img 
        :src="getImgUrl(movie.poster_path)"
        :lazy-src="getImgUrl(movie.poster_path)"
      >
        <template v-slot:placeholder>
          <v-row class="fill-height ma-0" align="center" justify="center">
            <v-progress-circular
              indeterminate
              color="grey lighten-5"
            ></v-progress-circular>
          </v-row>
        </template>
      </v-img>
      <v-card-title class="text-subtitle-1">
        {{ movie.title }}
      </v-card-title>
    </v-card>
  </div>
</template>

<script>

export default {
  name: 'MovieListItem',
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  methods: {
    selectMovie: function () {
      this.$emit('select-movie', this.movie)
    },
    getImgUrl: function (url) {
      const imgUrl = `https://image.tmdb.org/t/p/w300/${url}`
      return imgUrl
    },
  }
}
</script>

<style>

</style>