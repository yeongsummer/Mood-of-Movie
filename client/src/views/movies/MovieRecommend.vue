<template>
  <v-container style="width: 80vw; color:#2c3e50;">
    <!-- <h1 class="text-center" style="margin-bottom: 20px;">영화 추천</h1> -->
    <div style="margin-top: 50px;">
      <span class="subtitle" v-if="isLogin">{{nickname}} 님을 위한 추천 영화</span>
      <v-img
        v-if="isLogin"
        class="shrink mr-2"
        contain
        src='@/assets/movie.png'
        transition="scale-transition"
        height='40'
        style="display: inline-block;"
      />
    </div>
    <v-autocomplete
      v-if="isLogin"
      v-model="select"
      :loading="loading"
      :items="items"
      :search-input.sync="search"
      cache-items
      class="mx-5 my-5"
      flat
      hide-no-data
      hide-details
      color='green darken-1'
      label="인생 영화 제목을 입력하면 그와 유사한 영화를 추천해드립니다 :)"
      @keypress.enter="[flag=true, getRecommendedMovies(search)]"
    ></v-autocomplete>
    <recommend-List
      v-if="flag"
      :movieList="recommended_movies"
    />
    <div class="subtitle_container">
      <span class="subtitle">나를 힐링시켜줄 음악 영화</span>
      <v-img
        class="shrink mr-2"
        contain
        src='@/assets/music.png'
        transition="scale-transition"
        height='40'
        style="display: inline-block;"
      />
    </div>
    <recommend-List
      :movieList="recommend_movie_list[0]"
    />
    <div class="subtitle_container">
      <span class="subtitle">다가오는 크리스마스는 영화보면서 방콕 어때요?</span>
      <v-img
        class="shrink mr-2"
        contain
        src='@/assets/house.png'
        transition="scale-transition"
        height='40'
        style="display: inline-block;"
      />
    </div>
    <recommend-List
      :movieList="recommend_movie_list[1]"
    />
    <div class="subtitle_container">
      <span class="subtitle">시원한 액션보면서 스트레스를 날리자</span>
      <v-img
        class="shrink mr-2"
        contain
        src='@/assets/fight.png'
        transition="scale-transition"
        height='40'
        style="display: inline-block;"
      />
    </div>
    <recommend-List
      :movieList="recommend_movie_list[2]"
    />
    <div class="subtitle_container">
      <span class="subtitle">겨울이지만 바다는 보고싶어</span>
      <v-img
        class="shrink mr-2"
        contain
        src='@/assets/beach.png'
        transition="scale-transition"
        height='40'
        style="display: inline-block;"
      />
    </div>
    <recommend-List
      :movieList="recommend_movie_list[3]"
    />
    <div class="subtitle_container">
      <span class="subtitle">숨막히는 긴장감을 느껴봐 </span>
      <v-img
        class="shrink mr-2"
        contain
        src='@/assets/scared.png'
        transition="scale-transition"
        height='40'
        style="display: inline-block;"
      />
    </div>
    <recommend-List
      :movieList="recommend_movie_list[4]"
      style="margin-bottom:100px;"
    />
    
  </v-container>
</template>

<script>
import RecommendList from '@/components/RecommendList.vue'
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'MovieRecommend',
  components: {
    RecommendList
  },
  data: function () {
    return {
      movie_title: '',
      recommended_movies: [],
      flag: false,

      loading: false,
      items: [],
      search: null,
      select: null,
    }
  },
  computed: {
    ...mapState([
      'isLogin',
      'nickname',
      'recommend_movie_list',
      'movie_list'
    ])
  },
  watch: {
    search (val) {
      val && val !== this.select && this.querySelections(val)
    },
  },
  methods: {
    setToken: function () {
        const token = localStorage.getItem('jwt')
        const config = {
          Authorization: `JWT ${token}`
        }
        return config
    },
    getRecommendedMovies: function (movie_title) {
      console.log(movie_title)
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/movie_recommend/${movie_title}/`,
        headers: this.setToken()
        })
        .then(res => {
          this.recommended_movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    querySelections (v) {
      this.loading = true
      // Simulated ajax query
      setTimeout(() => {
        this.items = this.movie_list.filter(e => {
          return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
        })
        this.loading = false
      }, 500)
    },
  },
  // created() {
  //   console.log(this.recommend_movie_list.length)
  //   function get_default_movie(movie_title) {
  //       return axios ({
  //         method: 'get',
  //         url: `http://127.0.0.1:8000/movies/movie_recommend/${movie_title}/`
  //         })
  //     }
  //   if (this.recommend_movie_list.length != 5) {
  //     const default_movie = ['소울', '러브 액츄얼리', '캡틴 마블', '모아나', '텍사스 전기톱 연쇄살인사건']
  //     let recommendMovie = []

      
  //     Promise.all(default_movie.map(get_default_movie)).then(res => { 
  //       res.forEach((movies) => {
  //         recommendMovie.push(movies.data)
  //       this.$router.commit('GET_RECOMMEND_MOVIES', recommendMovie)
  //       })
  //     })
  //   }
  // }
}
</script>

<style scoped>
.maintitle {
  margin-top: 5%;
}

.subtitle_container {
  margin-top: 15%;
  margin-bottom: 2%;
}

.subtitle {
  color:#484848;
  font-size:30px; 
  font-weight: 700
}
</style>