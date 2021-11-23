<template>
  <v-container class="fill-height" fluid>
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

              <!-- <v-file-input
                @change="changeImg"
                outlined
                id="profile_img"
                label="프로필 이미지"
                name="profile_img"
                color="green lighten-3"
                placeholder="파일 선택"
                v-model="credentials.profile_img"
                prepend-icon=""
              ></v-file-input> -->

              *표시는 필수 입력 사항입니다.
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-form>
              <v-btn
                class="ma-2 white--text"
                color="green lighten-3"
                @click="signup"
              >
                회원 가입
              </v-btn>
            </v-form>
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
      is_pw: false,
      is_pw2: false,
      credentials: {
        email: null,
        password: null,
        passwordConfirmation: null,
        nickname: null,
        // profile_img: null,
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
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
      .then(res => {
        console.log(res)
        alert('회원가입이 완료되었습니다.')
        this.$router.push({ name: 'Login'})
      })
      .catch(err => {
        alert('회원가입 실패 : 회원 정보를 확인해주세요.')
        alert(err)
        console.log(err)
      })
    },
    // changeImg: function (files) {
    //   console.log(files)
    //   this.credentials.profile_img = files
    // },
  }
}
</script>

<style scoped>
#card {
  border: 2px solid #A5D6A7;
}
</style>