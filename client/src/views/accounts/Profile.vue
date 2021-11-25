<template>
  <v-container style="width: 80vw;">
    <v-row id="profile-box" class="mx-auto" align="center" justify="center" justify-center>
      <v-col
        cols="3"
      >
        <v-avatar size="200">
          <img :src="profile_img" alt="image" v-if="profile_img">
          <v-icon 
            v-if="!profile_img"
            color="green lighten-3"
            size="200"
          >mdi-account-circle</v-icon>
        </v-avatar>
      </v-col>
      <v-col
        cols="6"
      >
        <v-row style="margin: 10px;">
          <v-spacer></v-spacer>
          <h1>{{ $route.params.nickname }} 님의 프로필</h1>
          <v-spacer></v-spacer>
          <div v-if="$route.params.nickname != nickname">
            <v-btn 
              class="ma-2 white--text"
              color="green lighten-3"
              v-if="!followed"
              @click="[follow($route.params.nickname), followed=!followed]"
            >
              Follow
            </v-btn>
            <v-btn 
              class="ma-2 white--text"
              color="green lighten-3"
              elevation="0"
              v-if="followed"
              @click="[follow($route.params.nickname), followed=!followed]"
            >
              Unfollow
            </v-btn>
          </div>
          <div v-if="$route.params.nickname === nickname">
            <v-menu
              bottom
              min-width="150px"
              rounded
              offset-y
            >
              <template v-slot:activator="{ on }">
                <v-btn
                  class="ma-2 white--text"
                  color="green lighten-3"
                  elevation="0"
                  v-on="on"
                >
                  정보 수정
                </v-btn>
              </template>
              <v-card>
                <v-list-item-content class="justify-center">
                  <div class="mx-auto text-center">
                    <v-dialog
                      v-model="dialog1"
                      width="500"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn
                          depressed
                          text
                          v-bind="attrs"
                          v-on="on"
                        >
                          사진 업로드
                        </v-btn>
                      </template>

                      <v-card
                        id="card"
                        style="border-radius: 3px;"
                        border-color="green lighten-3"
                      >
                        <v-card-title class="text-h5 green lighten-3 white--text">
                          사진 업로드
                        </v-card-title>

                        <v-card-text style="margin-top: 30px;">
                          <v-file-input
                            outlined
                            id="profile_img"
                            label="프로필 이미지"
                            name="profile_img"
                            color="green lighten-3"
                            placeholder="파일 선택"
                            prepend-icon=""
                            accept="image/*"
                            :rules="[rules.image]"
                            @change="selectFile($event)"
                          ></v-file-input>
                        </v-card-text>

                        <v-divider></v-divider>

                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn
                            class="ma-2 white--text"
                            color="green lighten-3"
                            x-large
                            @click="[dialog1 = false, changeImg(image)]"
                          >
                            등록
                          </v-btn>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>

                    <v-divider class="my-3"></v-divider>

                    <v-dialog
                      v-model="dialog2"
                      width="500"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn
                          depressed
                          text
                          v-bind="attrs"
                          v-on="on"
                        >
                          비밀번호 변경
                        </v-btn>
                      </template>

                      <v-card
                        id="card"
                        style="border-radius: 3px;"
                        border-color="green lighten-3"
                      >
                        <v-card-title class="text-h5 green lighten-3 white--text">
                          비밀번호 변경
                        </v-card-title>

                        <v-card-text style="margin-top: 30px;">
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

                        <v-divider></v-divider>

                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn
                            class="ma-2 white--text"
                            color="green lighten-3"
                            x-large
                            @click="[dialog2 = false, changepassword(changepasswordData)]"
                          >
                            변경
                          </v-btn>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>
                  </div>
                </v-list-item-content>
              </v-card>
            </v-menu>
          </div>
          <v-spacer></v-spacer>
        </v-row>
        <v-row>
          <v-spacer></v-spacer>
          <v-col>
            <v-row>
              <h2>follower</h2>
            </v-row>
            <v-row>
              <v-menu
                bottom
                offset-y
                min-width="200px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    class="ma-2"
                    text
                    v-bind="attrs"
                    v-on="on"
                  >
                    <h3>{{ followers.length }}</h3>
                  </v-btn>
                </template>
                <v-list>
                  <v-list-item
                    v-for="(follower, i) in followers"
                    :key="i"
                  >
                    <v-list-item-title>
                      <v-btn text @click="$router.push({ name: 'Profile', params: {nickname: follower} })">
                        {{ follower }}
                      </v-btn>
                    </v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </v-row>
          </v-col>
          <v-col>
            <v-row>
              <h2>following</h2>
            </v-row>
            <v-row>
              <v-menu
                bottom
                offset-y
                min-width="200px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    class="ma-2"
                    text
                    v-bind="attrs"
                    v-on="on"
                  >
                    <h3>{{ followings.length }}</h3>
                  </v-btn>
                </template>
                <v-list>
                  <v-list-item
                    v-for="(following, i) in followings"
                    :key="i"
                  >
                    <v-list-item-title>
                      <v-btn text @click="$router.push({ name: 'Profile', params: {nickname: following} })">
                        {{ following }}
                      </v-btn>
                    </v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </v-row>
          </v-col>
          <v-spacer></v-spacer>
        </v-row>
      </v-col>
    </v-row>
    <v-divider light></v-divider>

    <div>
      <div class="title-box">
        <span style="font-size:30px; font-weight: 700">{{ $route.params.nickname }} 님이 찜한 영화</span>
        <v-img
          class="shrink mr-2"
          contain
          src='@/assets/heart.png'
          transition="scale-transition"
          height='40'
          style="display: inline-block;"
        />
      </div>
      <div class="background" :style="{'background-image': 'url('+require('@/assets/movie_list.png')+')'}">
        <v-slide-group
          class="pa-4"
          active-class="success"
          show-arrows
        >
          <v-slide-item
            v-for="movie in likeMovieList"
            :key="movie.id"
          >
            <like-movie-item
              :movie="movie"
            />
          </v-slide-item>
        </v-slide-group>
      </div>
    </div>

    <div>
      <div class="title-box">
        <span style="font-size:30px; font-weight: 700">{{ $route.params.nickname }} 님의 리뷰</span>
        <v-img
          class="shrink mr-2"
          contain
          src='@/assets/pencil.png'
          transition="scale-transition"
          height='40'
          style="display: inline-block;"
        />
      </div>
      <div v-if="my_reviews.length == 0" class="text-center">
        <h1>리뷰가 아직 없어요!</h1>
      </div>
      <review-list-item
        v-for="review in my_reviews" 
        :key="review.id"
        :review="review"
        @click.native="goReviewDetail(review.id)"
      />
    </div>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'
import { mapActions } from 'vuex'
import LikeMovieItem from '@/components/LikeMovieItem.vue'
import ReviewListItem from '@/components/ReviewListItem'
import axios from 'axios'

export default {
  name: 'Profile',
  components: {
    LikeMovieItem,
    ReviewListItem,
  },
  data: function () {
    return {
      dialog1: false,
      dialog2: false,
      password: null,
      followed: false,
      profileNickname: this.$route.params.nickname,
      image: null,
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
        nickname: value => !/[~!@#$%^&*()_+|<>?:{}]/.test(value) || "닉네임에는 특수문자를 사용할 수 없습니다.",
        image: value => !value || value.size < 2000000 || '프로필 사진은 2MB이하만 사용 가능합니다.'
      },
      passwordRules: [
        value => !!value || '필수 입력 사항입니다.',
        value => (value || "").length >= 6 & (value || "").length <= 15 || '비밀번호는 6~15글자이어야 합니다.',
        value => /[0-9]/.test(value) || '비밀번호는 숫자를 포함해야 합니다.',
        value => /[a-z]/.test(value) || '비밀번호는 영어를 포함해야 합니다.',
      ],
    }
  },
  methods: {
    ...mapActions([
      'moveToLink',
      'get_followers',
      'follow',
      'getMyReview',
      'changepassword'
    ]),
    goReviewDetail: function (review_pk) {
      this.$router.push({ name: "ReviewDetail", params: { review_pk: review_pk }})
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    selectFile(file) {
      // console.log('파일', file)
      let reader = new FileReader()
      reader.onload = (event) => {
        this.image = event.target.result
        console.log('이거', this.image)
      }
      reader.readAsDataURL(file)
    },
    changeImg(img) {
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/accounts/${this.nickname}/upload_img/`,
        data: {'profile_img': img},
        headers: this.setToken()
      })
      .then(res => {
        console.log(res)

        const data = {
        'id': this.userPk,
        'profile_img': img
        }
        this.$store.commit('USERIMGINFO', data)
      })
      .catch(err => {
        console.log(err)
      })
    },
  },
  computed: {
    ...mapState([
      'nickname',
      'followers',
      'followings',
      'profile_img',
      'likeMovieList',
      'my_reviews',
      'config',
      'userPk'
    ]),
  },
  created: function () {
    this.$store.dispatch('get_followers', this.profileNickname)
    this.$store.dispatch('get_followings', this.profileNickname)
    this.$store.dispatch('get_like_movies', this.profileNickname)
    this.$store.dispatch('getMyReview', this.profileNickname)

    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/${ this.profileNickname }/follow/`,
      headers: this.setToken()
      })
      .then(res => {
        // console.log('dlrj', res)
        this.followed = res.data.followed
      })
      .catch(err => {
        console.log(err)
      })
    
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.profileNickname}/upload_img/`,
        headers: this.setToken()
      })
      .then(res => {
        // console.log('이거', res)

        const data = {
        'id': res.data.id,
        'profile_img': res.data.profile_img
        }
        this.$store.commit('USERIMGINFO', data)
      })
      .catch(err => {
        console.log(err)
      })
  },
  watch: {
    '$route'() {
      this.$store.dispatch('get_followers', this.$route.params.nickname)
      this.$store.dispatch('get_followings', this.$route.params.nickname)
      this.$store.dispatch('get_like_movies', this.$route.params.nickname)
      this.$store.dispatch('getMyReview', this.$route.params.nickname)
      // console.log('여기', this.likeMovieList)

      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${ this.$route.params.nickname }/follow/`,
        headers: this.setToken()
        })
        .then(res => {
          // console.log('dlrj', res)
          this.followed = res.data.followed
        })
        .catch(err => {
          console.log(err)
        })
      
      axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/${this.$route.params.nickname}/upload_img/`,
          headers: this.setToken()
        })
        .then(res => {
          // console.log('이거', res)

          const data = {
          'id': res.data.id,
          'profile_img': res.data.profile_img
          }
          this.$store.commit('USERIMGINFO', data)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
}
</script>

<style>
#profile-box {
  width: 80%;
  margin-top: 3%;
  margin-bottom: 3%;
}

.background {
  width:100%;
  height: 100%;
  }

.title-box {
  margin-top: 10%;
  margin-bottom: 2%;
}

#card {
  border: 3px solid #A5D6A7;
}
</style>