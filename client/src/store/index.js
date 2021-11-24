import Vue from 'vue'
import Vuex from 'vuex'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    nickname: null,
    isLogin: false,
    userPk: null,
    comments: [],
    config: null,
    movie_list: [],
    recommend_movie_list:[],
    followers: [],
    followings: [],
    movie_ranking: [],
  },
  getters: {
  },
  mutations: {
    GET_RANKING: function (state, movies) {
      state.movie_ranking = movies
    },
    CREATE_COMMENT: function (state, commentItem) {
      state.comments.unshift(commentItem)
    },
    DELETE_COMMENT: function (state, commentItem) {
      const index = state.comments.indexOf(commentItem)
      state.comments.splice(index, 1)
    },
    GET_COMMENTS: function (state, comments) {
      state.comments = []
      comments.forEach(function(comment){
        const commentItem = {
          id: comment.id,
          content: comment.content,
          nickname: comment.user.nickname,
          created_at: comment.created_at
        }
        state.comments.unshift(commentItem)
      })
    },
    GET_MOVIES: function (state, movies) {
      state.movie_list = movies
    },
    GET_RECOMMEND_MOVIES: function (state, movies) {
      state.recommend_movie_list = movies
    },
    ISLOGIN: function (state, status) {
      state.isLogin = status
    },
    CONFIG: function (state, config) {
      state.config = config
    },
    USERINFO: function (state, data) {
      state.userPk = data.id
      state.nickname = data.nickname
    },
    UPDATEFOLLOW: function (state, data) {
      state.followers = data.followers
      state.followings = data.followings
    },
    ADDFOLLOW: function (state, user) {
      state.followers.push(user)
    }
  },
  actions: {
    moveToLink({ state }, routeObject) {
      state
      router.push(routeObject)
    },
    createComments({ commit }, commentItem) {
      commit('CREATE_COMMENT', commentItem)
    },
    deleteComments({ commit }, commentItem) {
      commit('DELETE_COMMENT', commentItem)
    },
    getComments({ commit }, comments) {
      commit('GET_COMMENTS', comments)
    },
    getRecommendMovies({ commit }, movies) {
      commit('GET_RECOMMEND_MOVIES', movies)
    },
    login: function ({ state, commit }, credentials) {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: credentials,
      })
      .then(res => {
        localStorage.setItem('jwt', res.data.token)
        commit('ISLOGIN', true)

        const token = localStorage.getItem('jwt')
        const config = {
          headers: {
            Authorization: `JWT ${token}`
          }
        }
        commit('CONFIG', config)

        axios.get(`http://127.0.0.1:8000/accounts/user/`, state.config)
          .then((res) => {
            // console.log(res.data)
            const id = res.data.id
            const nickname = res.data.nickname
            // console.log(nickname)
            commit('USERINFO', {'id': id, 'nickname': nickname})
          })
          .catch((err) => {
            console.log(err)
          })

        router.push({ name: 'MovieList' })
      })
      .catch(err => {
        console.log(err)
        alert('로그인 실패 : 로그인 정보를 확인해주세요.')
      })
      // 메인 페이지 영화 랭킹 가져오는 요청
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/',
        })
        .then(res => {
          commit('GET_RANKING', res.data)
        })
        .catch(err => {
          console.log(err)
        })

      // 자동완성 영화 데이터 가져오는 요청
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/all_movie/`,
        })
        .then(res => {
          commit('GET_MOVIES', res.data.movie_titles)
        })
        .catch(err => {
          console.log(err)
        })

      // 추천 페이지 영화 가져오는 요청
      const default_movie = ['소울', '러브 액츄얼리', '캡틴 마블', '모아나', '텍사스 전기톱 연쇄살인사건']
      let recommendMovie = []

      function get_default_movie(movie_title) {
        return axios ({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/movie_recommend/${movie_title}/`
          })
      }
      Promise.all(default_movie.map(get_default_movie)).then(res => { 
        console.log('이해가 안되네?', res)
        res.forEach((movies) => {
          recommendMovie.push(movies.data)
        commit('GET_RECOMMEND_MOVIES', recommendMovie)
        })
        // commit('GET_RECOMMEND_MOVIES', recommendMovie)
      })
      console.log(recommendMovie)
    },
    logout: function ({ commit }) {
      commit('ISLOGIN', false)
      commit('USERINFO', {'id': '', 'nickname': ''})
      localStorage.removeItem('jwt')
      router.push({ name: 'Login' })
    },
    changepassword({ state }, changepasswordData) {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
       }
      }
      axios.post(`http://127.0.0.1:8000/accounts/${ state.userPk }/password/`, changepasswordData, config)
        .then(() => {
          alert('비밀번호가 변경되었습니다.')
          router.push({ name: 'Profile'})
        })
        .catch(err => console.error(err))
    },
    get_follow: function ({ state, commit }, nickname) {
      axios.get(`http://127.0.0.1:8000/accounts/${ nickname }/get_follow/`, state.config)
        .then((res) => {
          // console.log(res.data)
          const followers = res.data.followers
          const followings = res.data.followings
          commit('UPDATEFOLLOW', {'followers': followers, 'followings': followings})
        })
        .catch((err) => {
          console.log(err)
        })
    },
    follow: function ({ state, commit }, nickname) {
      axios.post(`http://127.0.0.1:8000/accounts/${ nickname }/follow/`, null, state.config)
      .then(res => {
        res
        console.log('여기!')
        // 여기를 닉네임으로? 객체로?
        commit('ADDFOLLOW', state.nickname)
      })
      .catch(err => {
        console.log(err)
      })
    },
  },
  plugins: [
    createPersistedState()
  ]
})
