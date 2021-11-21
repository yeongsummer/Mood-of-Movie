<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card class="elevation-12">
          <v-card-text>
            <v-form>
              <v-text-field
                id="user_id"
                label="아이디"
                name="user_id"
                type="text"
                v-model="credentials.username"
              ></v-text-field>

              <v-text-field
                id="password"
                label="비밀번호"
                name="password"
                type="password"
                @keypress.enter="login"
                v-model="credentials.password"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn
              class="ma-2 white--text"
              color="light-green lighten-2"
              @click="login"
            >
              로그인
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
      .then(res => {
        localStorage.setItem('jwt', res.data.token)
        this.$emit('login')
        this.$router.push({ name: 'TodoList' })
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>