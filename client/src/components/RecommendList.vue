<template>
<div class="list_container">
  <div class="background" :style="{'background-image': 'url('+require('@/assets/movie_list.png')+')'}">
    <v-slide-group
      class="pa-4"
      active-class="success"
      show-arrows
    >
      <v-slide-item
        v-for="movie in movieList"
        :key="movie.id"
      >
        <recommend-item
          :movie="movie"
        />
      </v-slide-item>
    </v-slide-group>
  </div>
</div>
</template>

<script>
import RecommendItem from '@/components/RecommendItem.vue'

export default {
  components: { RecommendItem },
  name: "RecommendList",
  props: {
    movieList: Array,
  },
}
</script>

<style>
.background {
  width:100%;
  height: 100%;
  }
.list_container {
  width: 100%;
  height: 100%;
}
</style>