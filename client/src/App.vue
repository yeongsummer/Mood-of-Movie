<template>
  <v-app>
    <app-navbar/>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'App',

  components: {
    appNavbar: Navbar,
  },

  data: () => ({
    //
  }),
};
</script>
