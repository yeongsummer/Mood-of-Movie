<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card class="elevation-12">
          <v-card-text>
            <v-form>
              <v-text-field
                id="user_id"
                label="이메일"
                name="user_id"
                type="email"
                v-model="credentials.userId"
              ></v-text-field>

              <v-text-field
                id="password"
                label="비밀번호"
                name="password"
                type="password"
                v-model="credentials.password"
              ></v-text-field>

              <v-text-field
                id="passwordConfirm"
                label="비밀번호 확인"
                name="passwordConfirm"
                type="password"
                v-model="credentials.passwordConfirm"
              ></v-text-field>

              <v-text-field
                id="nickname"
                label="닉네임"
                name="nickname"
                type="text"
                v-model="credentials.nickname"
              ></v-text-field>

              <v-text-field
                id="profile"
                label="프로필 이미지"
                name="profile"
                type="text"
                v-model="credentials.profile"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn
              class="ma-2 white--text"
              color="green lighten-3"
              @click="signup"
            >
              회원 가입
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
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        userId: null,
        password: null,
        passwordConfirm: null,
        nickname: null,
        profile: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
      .then(res => {
        console.log(res)
        this.$router.push({ name: 'Login'})
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>