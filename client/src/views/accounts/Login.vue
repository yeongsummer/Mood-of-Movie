<template>
  <v-container id="container" class="fill-height" fluid :style="{'background-image': 'url('+require('@/assets/background.png')+')'}">
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card 
          id="card"
          class="rounded-lg"
          border-color="green lighten-3"
        >
          <v-card-text>
            <v-form>
              <v-text-field
                outlined
                id="email"
                label="아이디"
                name="email"
                type="email"
                color="green lighten-3"
                v-model="credentials.email"
                :rules="[rules.required]"
              ></v-text-field>

              <v-text-field
                outlined
                id="password"
                label="비밀번호"
                name="password"
                :append-icon="is_pw ? 'mdi-eye' : 'mdi-eye-off'"
                :type="is_pw ? 'text' : 'password'"
                @click:append="is_pw = !is_pw"
                color="green lighten-3"
                @keypress.enter="login"
                v-model="credentials.password"
                :rules="[rules.required]"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn
              class="ma-2 white--text"
              color="green lighten-3"
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
      is_pw: false,
      credentials: {
        email: null,
        password: null,
      },
      rules: {
        required: value => !!value || '필수 입력 사항입니다.',
      },
    }
  },
  methods: {
    // userid가 필요한지?
    // setToken: function () {
    //   const token = localStorage.getItem('jwt')
    //   const config = {
    //     headers: {
    //       Authorization: `JWT ${token}`
    //     }
    //   }
    //   return config
    // },

    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
      .then(res => {
        localStorage.setItem('jwt', res.data.token)
        this.$emit('login')
        this.$store.state.isLogin = true
        this.$store.state.username = this.credentials.username

        // const config = this.setToken()
        // axios.get('http://127.0.0.1:8000/accounts/user/', config)
        //   .then((res) => {
        //     console.log(res)
        //     console.log(res.data)
        //     const id = res.data
        //     this.$store.state.login_user = id
        //   })
        //   .catch((err) => {
        //     console.log(err)
        //   })

        this.$router.push({ name: 'MovieList' })
      })
      .catch(err => {
        console.log(err)
        alert('로그인 실패 : 로그인 정보를 확인해주세요.')
      })
    },
  },
}
</script>

<style scoped>
#container {
  background-size: 100% 100%;
}

#card {
  border: 2px solid #A5D6A7;
}
</style>