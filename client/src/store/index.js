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
    profile_img: false,
    comments: [],
    config: null,
    movie_list: [],
    recommend_movie_list:[],
    followers: [],
    followings: [],
    likeMovieList: [],
    movie_ranking: [],
    my_reviews: [],
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
    USERIMGINFO: function (state, data) {
      state.userPk = data.id
      state.profile_img = data.profile_img
    },
    UPDATEFOLLOWER: function (state, data) {
      state.followers = data.followers
    },
    UPDATEFOLLOWING: function (state, data) {
      state.followings = data.followings
    },
    UPDATELIEKMOVIE: function (state, data) {
      // console.log(data.like_movies)
      state.likeMovieList = data.like_movies
    },
    UPDATEMYREVIEW: function (state, data) {
      // console.log(data)
      state.my_reviews = data.my_reviews
    },
    ADDFOLLOW: function (state, user) {
      state.followers.push(user)
    },
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
        alert('????????? ?????? : ????????? ????????? ??????????????????.')
      })
      // ?????? ????????? ?????? ?????? ???????????? ??????
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

      // ???????????? ?????? ????????? ???????????? ??????
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

      // ?????? ????????? ?????? ???????????? ??????
      const default_movie = ['??????', '?????? ????????????', '?????? ??????', '?????????', '????????? ????????? ??????????????????']
      let recommendMovie = []

      function get_default_movie(movie_title) {
        return axios ({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/movie_recommend/${movie_title}/`
          })
      }
      Promise.all(default_movie.map(get_default_movie)).then(res => { 
        // console.log('????????? ??????????', res)
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
      router.push({ name: 'MovieList'})
    },
    changepassword({ state }, changepasswordData) {
      state
      const token = localStorage.getItem('jwt')
      const config = {
          Authorization: `JWT ${token}`
      }
      axios({
        method: 'put',
        url: 'http://127.0.0.1:8000/accounts/password/',
        data: changepasswordData,
        headers: config
      })
      .then((res) => {
        console.log(res)
        alert('??????????????? ?????????????????????.')
      })
      .catch(err => console.error(err))
    },
    get_followers: function ({ state, commit }, nickname) {
      axios.get(`http://127.0.0.1:8000/accounts/${ nickname }/get_followers/`, state.config)
        .then((res) => {
          const followers = []
          for (let follower of res.data) {
            followers.push(follower.nickname)
          }
          commit('UPDATEFOLLOWER', {'followers': followers})
        })
        .catch((err) => {
          console.log(err)
        })
    },
    get_followings: function ({ state, commit }, nickname) {
      axios.get(`http://127.0.0.1:8000/accounts/${ nickname }/get_followings/`, state.config)
        .then((res) => {
          const followings = []
          for (let following of res.data) {
            followings.push(following.nickname)
          }
          commit('UPDATEFOLLOWING', {'followings': followings})
        })
        .catch((err) => {
          console.log(err)
        })
    },
    get_like_movies: function ({ state, commit }, nickname) {
      axios.get(`http://127.0.0.1:8000/accounts/${ nickname }/get_like_movies/`, state.config)
        .then((res) => {
          // console.log(res.data)
          const like_movies = []
          for (let movie of res.data) {
            like_movies.push(movie)
          }
          commit('UPDATELIEKMOVIE', {'like_movies': like_movies})
        })
        .catch((err) => {
          console.log(err)
        })
    },
    follow: function ({ state, commit }, nickname) {
      axios.post(`http://127.0.0.1:8000/accounts/${ nickname }/follow/`, null, state.config)
      .then(res => {
        res
        // get_followers
        axios.get(`http://127.0.0.1:8000/accounts/${ nickname }/get_followers/`, state.config)
        .then((res) => {
          const followers = []
          for (let follower of res.data) {
            followers.push(follower.nickname)
          }
          commit('UPDATEFOLLOWER', {'followers': followers})
        })
        .catch((err) => {
          console.log(err)
        })
        // get_followings
        axios.get(`http://127.0.0.1:8000/accounts/${ nickname }/get_followings/`, state.config)
        .then((res) => {
          const followings = []
          for (let following of res.data) {
            followings.push(following.nickname)
          }
          commit('UPDATEFOLLOWING', {'followings': followings})
        })
        .catch((err) => {
          console.log(err)
        })
      })
      .catch(err => {
        console.log(err)
      })
    },
    getMyReview: function ({ state, commit }, nickname) {
      axios.get(`http://127.0.0.1:8000/accounts/${ nickname }/review_list/`, state.config)
        .then(res => {
          // console.log(res)
          const my_reviews = res.data
          commit('UPDATEMYREVIEW', {'my_reviews': my_reviews})
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
