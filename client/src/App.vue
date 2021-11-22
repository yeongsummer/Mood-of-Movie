<template>
  <v-app>
    <navbar/>
    <v-main style="padding-top: 0px;">
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'App',

  components: {
    Navbar,
  },
}
</script>

<style>
  #nav {
    text-align: center;
    padding: 30px;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }

  #nav a.router-link-exact-active {
    color: #42b983;
  }

  #main {
    padding-top: 0px;
  }
</style>