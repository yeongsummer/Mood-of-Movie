<template>
  <div class="navbar">
    <v-app-bar
      app
      color="white"
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
        <v-btn text>
          <router-link :to="{ name: 'Password' }" class="text-btn">Password</router-link> 
        </v-btn>
        <v-btn text>
          <router-link @click.native="logout" to="#" class="text-btn">Logout</router-link>
        </v-btn>
      </span>
      <span v-else>
        <v-btn text>
          <router-link :to="{ name: 'Login' }" class="text-btn">Login</router-link> 
        </v-btn>
        <v-btn text>
          <router-link :to="{ name: 'Signup' }" class="text-btn">Signup</router-link>
        </v-btn>
        <v-btn text>
          <router-link to="#" class="text-btn">Profile</router-link>
        </v-btn>
      </span>
      <v-btn text>
        <router-link to="#" class="text-btn">Search</router-link>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view @login="isLogin=true"/>
    </v-main>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false,
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    
    if (token) {
      this.isLogin = true
    }
  }
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