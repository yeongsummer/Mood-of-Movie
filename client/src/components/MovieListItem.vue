<template>
  <v-dialog
    v-model="dialog"
    width="600px"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-col md="3">
        <v-card 
          class="mx-auto mb-10" 
          max-width="200" 
          v-bind="attrs"
          v-on="on"
        >
          <v-img
            :src="getImgUrl(movie.poster_path)"
            :lazy-src="getImgUrl(movie.poster_path)"
            max-height="290"
            class="my-auto"
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
          <v-card-text class="fw-bold text-start text-nowrap overflow-hidden">
            {{ movie.title }}
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn icon><v-icon>bookmark</v-icon></v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </template>
    <v-card>
      <v-img 
        :src="getImgUrl(movie.poster_path)"
        :lazy-src="getImgUrl(movie.poster_path)"
        max-width="200"
        class = "ma-4"
      >
      </v-img>
      <v-card-title>
        <span class="text-h5">{{ movie.title }}</span>
      </v-card-title>
      <v-card-text>
        {{ movie.directors }}
      </v-card-text>
      <v-card-text>
        {{ movie.overview }}
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="green darken-1"
          text
          @click="goReview"
        >
          리뷰보러가기
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
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
    getImgUrl: function (url) {
      const imgUrl = `https://image.tmdb.org/t/p/w300/${url}`
      return imgUrl
    },
    goReview: function () {
      this.$router.push({ name: 'ReviewList', query: { movie: this.movie } })
    }
  }
}
</script>

<style>

</style>