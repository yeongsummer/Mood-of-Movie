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
  },
  getters: {
  },
  mutations: {
    CREATE_COMMENT: function (state, commentItem) {
      state.comments.unshift(commentItem)
    },
    GET_COMMENTS: function (state, comments) {
      state.comments = comments
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
  },
  actions: {
    moveToLink({ state }, routeObject) {
      state
      router.push(routeObject)
    },
    createComments({ commit }, commentItem) {
      commit('CREATE_COMMENT', commentItem)
    },
    getComments({ commit }, comments) {
      commit('GET_COMMENTS', comments)
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

        axios.get('http://127.0.0.1:8000/accounts/user/', state.config)
          .then((res) => {
            console.log(res.data)
            const id = res.data.id
            const nickname = res.data.nickname
            console.log(nickname)
            commit('USERINFO', {'id': id, 'nickname': nickname})
          })
          .catch((err) => {
            console.log(err)
          })

        this.$router.push({ name: 'MovieList' })
      })
      .catch(err => {
        console.log(err)
        alert('로그인 실패 : 로그인 정보를 확인해주세요.')
      })
    },
    logout: function () {
      commit('ISLOGIN', false)
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
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
  },
  plugins: [
    createPersistedState()
  ]
})
