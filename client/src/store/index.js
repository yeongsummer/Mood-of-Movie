import Vue from 'vue'
import Vuex from 'vuex'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate';


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    nickname: null,
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
  },
  plugins: [
    createPersistedState()
  ]
})
