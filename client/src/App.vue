<template>
  <v-app>
    <Navbar/>
    <v-main>
      <div id="nav">
        <span>
          <router-link :to="{ name: 'MovieList' }" class="text-btn">Ranking</router-link> | 
          <router-link :to="{ name: 'MovieRecommend' }" class="text-btn">Recommend</router-link>
        </span>
      </div>
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
</style>