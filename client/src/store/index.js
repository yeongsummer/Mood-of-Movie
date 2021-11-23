import Vue from 'vue'
import Vuex from 'vuex'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate';


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    email: null,
    login: false,
    login_user: null,
    comments: [],
  },
  mutations: {
    CREATE_COMMENT: function (state, commentItem) {
      state.comments.unshift(commentItem)
    },
    GET_COMMENTS: function (state, comments) {
      state.comments = comments
    },
    IS_LOGIN: function (state, email) {
      state.email = email
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
    isLogin({ commit }, email) {
      commit('IS_LOGIN', email)
    }
  },
  plugins: [
    createPersistedState()
  ]
})
