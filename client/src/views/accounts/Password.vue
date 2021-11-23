<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card class="elevation-12">
          <v-card-text>
            <v-form>
              <v-text-field
                outlined
                id="old_password"
                label="기존 비밀번호"
                name="old_password"
                :append-icon="is_pw ? 'mdi-eye' : 'mdi-eye-off'"
                :type="is_pw ? 'text' : 'password'"
                @click:append="is_pw = !is_pw"
                color="green lighten-3"
                v-model="changepasswordData.old_password"
                @keypress.enter="changepassword(changepasswordData)"
                :rules="[rules.required]"
              ></v-text-field>

              <v-text-field
                outlined
                id="new_password1"
                label="새 비밀번호"
                name="new_password1"
                :append-icon="is_pw2 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="is_pw2 ? 'text' : 'password'"
                @click:append="is_pw2 = !is_pw2"
                color="green lighten-3"
                v-model="changepasswordData.new_password1"
                @keypress.enter="changepassword(changepasswordData)"
                :rules="passwordRules"
              ></v-text-field>

              <v-text-field
                outlined
                id="new_password2"
                label="새 비밀번호 확인"
                name="new_password2"
                :append-icon="is_pw3 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="is_pw3 ? 'text' : 'password'"
                @click:append="is_pw3 = !is_pw3"
                color="green lighten-3"
                v-model="changepasswordData.new_password2"
                @keypress.enter="changepassword(changepasswordData)"
                :rules="[rules.required, rules.confirm]"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn
              class="ma-2 white--text"
              color="green lighten-3"
              @click="changepassword(changepasswordData)"
            >
              변경 하기
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "changepassword",
  data() {
    return {
      is_pw: false,
      is_pw2: false,
      is_pw3: false,
      changepasswordData: {
        old_password: null,
        new_password1: null,
        new_password2: null,
      },
      rules: {
        required: value => !!value || '필수 입력 사항입니다.',
        confirm: value => value === this.changepasswordData.new_password1 || '비밀번호가 일치하지 않습니다.'
      },
      passwordRules: [
        value => !!value || '필수 입력 사항입니다.',
        value => (value || "").length >= 6 & (value || "").length <= 15 || '비밀번호는 6~15글자이어야 합니다.',
        value => /[0-9]/.test(value) || '비밀번호는 숫자를 포함해야 합니다.',
        value => /[a-z]/.test(value) || '비밀번호는 영어를 포함해야 합니다.',
      ],
    };
  },
  methods: {
    ...mapActions(["changepassword"])
  }
};
</script>

<style scoped>
</style>