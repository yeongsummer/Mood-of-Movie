<template>
  <div class="navbar">
    <v-app-bar
      app
      color="white"
      elevation="0"
    >
      <v-spacer></v-spacer>

      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />
      </div>
      <v-spacer></v-spacer>

      <span v-if="isLogin">
        <v-btn text @click="logout()">Logout</v-btn>
        <!-- 여기에 닉네임 넣는 방법!!! -->
        <v-btn icon @click="moveToLink({ name: 'Profile', params: {nickname: 'aa'} })">
          <v-icon>mdi-account</v-icon>
        </v-btn>
      </span>
      <span v-else>
        <v-btn text @click="moveToLink({ name: 'Login' })">Login</v-btn>
        <v-btn text @click="moveToLink({ name: 'Signup' })">Signup</v-btn>
      </span>
    </v-app-bar>

    <v-main>
      <router-view @login="isLogin=true"/>
    </v-main>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { mapActions } from 'vuex'

export default {
  name: 'Navbar',
  data: function () {
    return {
    }
  },
  methods: {
    ...mapActions([
      'moveToLink',
      'logout'
    ]),
  },
  computed: {
    ...mapState([
      'isLogin',
      'nickname',
      'userPk',
    ])
  },
}
</script>

<style scoped>
.navbar{
  display:inline-flex;
  position:relative;
  overflow:hidden;
  max-width:100%;
  height: 48px;
  background-color:white;
  padding:0 20px;
}

.text-btn {
  color:#000;
  text-decoration:none;
}
</style>