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
        <v-dialog
          v-model="loginDialog"
          width="550px"
          transition="dialog-top-transition"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn 
              text 
              v-bind="attrs"
              v-on="on"
            >Login</v-btn>
          </template>
          <v-card 
            id="card"
            class="rounded-lg"
            border-color="green lighten-3"
          >
            <v-card-title class="text-h5 green lighten-3 white--text">
              LOGIN
            </v-card-title>
            <v-card-text style="margin-top: 30px;">
              <v-form>
                <v-text-field
                  outlined
                  id="email"
                  label="아이디"
                  name="email"
                  type="email"
                  color="green lighten-3"
                  v-model="login_credentials.email"
                  :rules="[rules.required]"
                ></v-text-field>

                <v-text-field
                  outlined
                  id="password"
                  label="비밀번호"
                  name="password"
                  :append-icon="is_pw3 ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="is_pw3 ? 'text' : 'password'"
                  @click:append="is_pw3 = !is_pw3"
                  color="green lighten-3"
                  @keypress.enter="login"
                  v-model="login_credentials.password"
                  :rules="[rules.required]"
                ></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                class="ma-2 white--text"
                color="green lighten-3"
                x-large
                @click="[loginDialog = false, login(login_credentials)]"
              >
                로그인
              </v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog
          v-model="signupDialog"
          width="550px"
          transition="dialog-top-transition"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn 
              text 
              v-bind="attrs"
              v-on="on"
            >Signup</v-btn>
          </template>
          <v-card 
            id="card"
            class="rounded-lg"
            border-color="green lighten-3"
          >
            <v-card-title class="text-h5 green lighten-3 white--text">
              SIGNUP
            </v-card-title>
            <v-card-text style="margin-top: 30px;">
              <v-form>
                <v-text-field
                  outlined
                  id="email-other"
                  label="*이메일"
                  name="email"
                  type="email"
                  color="green lighten-3"
                  v-model="credentials.email"
                  :rules="[rules.required, rules.email]"
                ></v-text-field>

                <v-text-field
                  outlined
                  id="password"
                  label="*비밀번호"
                  hint="영어, 숫자를 혼합하여 작성해주세요. (6~15글자)"
                  name="password"
                  :append-icon="is_pw ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="is_pw ? 'text' : 'password'"
                  @click:append="is_pw = !is_pw"
                  color="green lighten-3"
                  v-model="credentials.password"
                  :rules="passwordRules"
                ></v-text-field>

                <v-text-field
                  outlined
                  id="passwordConfirmation"
                  label="*비밀번호 확인"
                  hint="확인을 위해 위와 동일한 비밀번호를 입력해주세요."
                  name="passwordConfirmation"
                  :append-icon="is_pw2 ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="is_pw2 ? 'text' : 'password'"
                  @click:append="is_pw2 = !is_pw2"
                  color="green lighten-3"
                  v-model="credentials.passwordConfirmation"
                  :rules="[rules.required, rules.confirm]"
                ></v-text-field>

                <v-text-field
                  outlined
                  id="nickname"
                  label="*닉네임"
                  hint="특수문자를 제외한 한글/영문/숫자만 입력해주세요."
                  name="nickname"
                  type="text"
                  color="green lighten-3"
                  v-model="credentials.nickname"
                  :rules="[rules.required, rules.nickname]"
                ></v-text-field>

                *표시는 필수 입력 사항입니다.
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                class="ma-2 white--text"
                color="green lighten-3"
                x-large
                @click="[signupDialog = false, signup()]"
              >
                회원 가입
              </v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </span>
    <v-btn text @click="test()">Test</v-btn>
    
    </v-app-bar>

    <v-main>
      <router-view @login="isLogin=true"/>
    </v-main>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { mapActions } from 'vuex'
import axios from 'axios'

export default {
  name: 'Navbar',
  data: function () {
    return {
      loginDialog: false,
      signupDialog: false,
      is_pw: false,
      is_pw2: false,
      is_pw3: false,
      login_credentials: {
        email: null,
        password: null,
      },
      credentials: {
        email: null,
        password: null,
        passwordConfirmation: null,
        nickname: null,
      },
      rules: {
        required: value => !!value || '필수 입력 사항입니다.',
        email: value => /.+@.+\..+/.test(value) || '이메일 형식으로 입력해주세요.',
        nickname: value => !/[~!@#$%^&*()_+|<>?:{}]/.test(value) || "닉네임에는 특수문자를 사용할 수 없습니다.",
        confirm: value => value === this.credentials.password || '비밀번호가 일치하지 않습니다.'
      },
      passwordRules: [
        value => !!value || '필수 입력 사항입니다.',
        value => (value || "").length >= 6 & (value || "").length <= 15 || '비밀번호는 6~15글자이어야 합니다.',
        value => /[0-9]/.test(value) || '비밀번호는 숫자를 포함해야 합니다.',
        value => /[a-z]/.test(value) || '비밀번호는 영어를 포함해야 합니다.',
        // value => /[`~!@@#$%^&*|₩₩₩'₩";:₩/?]/.test(value) || '비밀번호는 특수문자를 포함해야 합니다.',
      ],
    }
  },
  methods: {
    ...mapActions([
      'moveToLink',
      'login',
      'logout',
    ]),

    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
      .then(res => {
        console.log(res)
        alert('회원가입이 완료되었습니다.')
      })
      .catch(err => {
        alert('회원가입 실패 : 회원 정보를 확인해주세요.')
        console.log(err)
      })
    },

    test: function () {
      console.log(this.userPk)
      axios.get(`http://127.0.0.1:8000/accounts/${this.userPk}/user_profile_update_delete/`, this.config)
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    },

  },
  computed: {
    ...mapState([
      'isLogin',
      'nickname',
      'userPk',
      'config'
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

#card {
  border: 3px solid #A5D6A7;
}
</style>