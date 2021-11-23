import Vue from 'vue'
import Vuex from 'vuex'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'
// import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username: null,
    islogin: false,
    // login_user: null,
    comments: [],
  },
  getters: {
  },
  mutations: {
    CREATE_COMMENT: function (state, commentItem) {
      state.comments.unshift(commentItem)
    },
    GET_COMMENTS: function (state, comments) {
      state.comments = comments
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
    getComments({ commit }, comments) {
      commit('GET_COMMENTS', comments)
    },
    // changepassword({ getters }, changepasswordData) {
    //   axios.post(SERVER.URL + SERVER.ROUTES.accounts.changePassword, changepasswordData, getters.config)
    //     .then(() => {
    //       alert('비밀번호가 변경되었습니다.')
    //       router.push({ name: 'UserDetailView'})
    //     })
    //     .catch(err => console.error(err))
    // },
  },
  plugins: [
    createPersistedState()
  ]
})
