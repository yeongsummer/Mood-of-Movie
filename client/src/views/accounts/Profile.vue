<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <v-img id="user-profile" src="@/assets/default.jpg"></v-img>
        <v-menu
          bottom
          min-width="150px"
          rounded
          offset-y
        >
          <template v-slot:activator="{ on }">
            <v-btn
              elevation="0"
              icon
              outlined
              small
              v-on="on"
            >
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </template>
          <v-card>
            <v-list-item-content class="justify-center">
              <div class="mx-auto text-center">
                <v-btn
                  depressed
                  text
                >
                  사진 업로드
                </v-btn>
                <v-divider class="my-3"></v-divider>
                <v-btn
                  depressed
                  text
                  @click="moveToLink({ name: 'Password' })"
                >
                  비밀번호 변경
                </v-btn>
              </div>
            </v-list-item-content>
          </v-card>
        </v-menu>
      </v-col>
      <v-col>
        <h1>{{ $route.params.nickname }}님의 프로필</h1>
        <p>follower {{ followers }}</p>
        <p>following {{ followings }}</p>
        <v-btn 
          text
          @click="follow($route.params.nickname)"
        >
          Follow
        </v-btn>
      </v-col>
    </v-row>
    <v-divider></v-divider>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'
import { mapActions } from 'vuex'

export default {
  name: 'Profile',
  methods: {
    ...mapActions([
      'moveToLink',
      'get_follow',
      'follow'
    ]),
  },
  computed: {
    ...mapState([
      'nickname',
      'followers',
      'followings'
    ])
  },
  created: function () {
    this.get_follow(this.route.params.nickname)
  }
}
</script>

<style>
#user-profile {
  width: 200px;
}
</style>