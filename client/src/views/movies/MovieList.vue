<template>
  <v-container style="width: 80vw;">
    <div class="background" :style="{'background-image': 'url('+require('@/assets/main_image.jpg')+')','width':'100%'}">
      <div class="main_text">
        <p>지금 나에게 맞는 영화를 찾고,</p>
        <p>나만의 영화 경험을 공유하세요.</p>
      </div>
    </div>
    <p class="text-center" style="margin: 20px; font-size: 4vw; font-weight:700; text-shadow:6px 6px #f1cb70">TOP 20</p>
    <v-row no-gutters class="justify-center background2" :style="{'background-image': 'url('+require('@/assets/list_cover.png')+')','width':'100%'}">
      <movie-list-item 
        v-for="(movie,index) in movie_ranking" 
        :key="index"
        :index="index"
        :movie="movie"
      >
      </movie-list-item>
    </v-row>
  </v-container>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'
import { mapState } from 'vuex'

import axios from 'axios'
// import _ from 'lodash'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  data: function () {
    return {
      active_tab: 0,
      movies: {
        type: Array,
        required: true
      }
    }
  },
  computed: {
    ...mapState([
      'movie_ranking'
    ])
  },
  methods: {
  },
  created: function () {
    if (this.movie_ranking.length != 20) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/',
        })
        .then(res => {
          this.$router.commit('GET_RANKING', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  mounted() {
    this.active_tab = 1;
  }
}
</script>

<style>
.background {
  background-size: 100% 100%;
  margin-bottom: 10vh;
}

.background2 {
  background-size: 100% 100%;
  padding: 30px;
  margin-bottom: 10vh;
}

.main_text{
  margin-left: 50px;
  padding-top: 20%;
  padding-bottom: 15%;
  color: white;
  font-size: 2.5vw;
  font-weight: 700;
}
</style>