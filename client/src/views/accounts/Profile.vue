<template>
  <v-container>
    <v-row id="profile-box" align="center" justify="center" justify-center>
      <v-col>
        <v-menu
          bottom
          min-width="150px"
          rounded
          offset-y
        >
          <template v-slot:activator="{ on }">
            <v-btn
              icon
              elevation="0"
              outlined
              v-on="on"
            >
              <v-avatar size="200">
                <v-img src="@/assets/default.jpg"></v-img>
              </v-avatar>
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

                  <v-card>
                    <v-card-title class="text-h5 grey lighten-2">
                      사진 업로드
                    </v-card-title>

                    <v-card-text>
                      <v-file-input
                        outlined
                        id="profile_img"
                        label="프로필 이미지"
                        name="profile_img"
                        color="green lighten-3"
                        placeholder="파일 선택"
                        v-model="profile_img"
                        prepend-icon=""
                      ></v-file-input>
                    </v-card-text>

                    <v-divider></v-divider>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="primary"
                        text
                        @click="[dialog1 = false, changeImg(profile_img)]"
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

                  <v-card>
                    <v-card-title class="text-h5 grey lighten-2">
                      비밀번호 변경
                    </v-card-title>

                    <v-card-text>
                      <v-text-field
                        outlined
                        id="password"
                        label="*닉네임"
                        hint="특수문자를 제외한 한글/영문/숫자만 입력해주세요."
                        name="password"
                        type="text"
                        color="green lighten-3"
                        v-model="password"
                        :rules="[rules.required, rules.nickname]"
                      ></v-text-field>
                    </v-card-text>

                    <v-divider></v-divider>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="primary"
                        text
                        @click="dialog2 = false"
                      >
                        변경
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>

                <!-- <v-btn
                  depressed
                  text
                  @click="moveToLink({ name: 'Password' })"
                >
                  비밀번호 변경
                </v-btn> -->
              </div>
            </v-list-item-content>
          </v-card>
        </v-menu>
      </v-col>
      <v-col>
        <v-row style="margin: 10px;">
          <h1>{{ $route.params.nickname }} 님의 프로필</h1>
          <v-btn 
            class="ma-2 white--text"
            color="green lighten-3"
            @click="follow($route.params.nickname)"
          >
            Follow
          </v-btn>
        </v-row>
        <v-row>
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
                    <v-list-item-title>{{ follower }}</v-list-item-title>
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
                    <v-list-item-title>{{ following }}</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </v-row>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-divider></v-divider>
    <h2>{{ $route.params.nickname }} 님이 찜한 영화</h2>
    <div>
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
    <h2>{{ $route.params.nickname }} 님의 리뷰</h2>
    <div v-if="my_reviews.length == 0" class="text-center">
      <h1>리뷰가 아직 없어요!</h1>
    </div>
    <review-list-item
      v-for="review in my_reviews" 
      :key="review.id"
      :review="review"
      @click.native="goReviewDetail(review.id)"
    />
  </v-container>
</template>

<script>
import { mapState } from 'vuex'
import { mapActions } from 'vuex'
import LikeMovieItem from '@/components/LikeMovieItem.vue'
import ReviewListItem from '@/components/ReviewListItem'

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
      profileNickname: this.$route.params.nickname,
      rules: {
        required: value => !!value || '필수 입력 사항입니다.',
        nickname: value => !/[~!@#$%^&*()_+|<>?:{}]/.test(value) || "닉네임에는 특수문자를 사용할 수 없습니다.",
      },
    }
  },
  methods: {
    ...mapActions([
      'moveToLink',
      'get_followers',
      'follow',
      'getMyReview',
    ]),
    goReviewDetail: function (review_pk) {
      this.$router.push({ name: "ReviewDetail", params: { review_pk: review_pk }})
    },
  },
  computed: {
    ...mapState([
      'nickname',
      'followers',
      'followings',
      'profile_img',
      'likeMovieList',
      'my_reviews'
    ])
  },
  created: function () {
    this.$store.dispatch('get_followers', this.profileNickname)
    this.$store.dispatch('get_followings', this.profileNickname)
    this.$store.dispatch('get_like_movies', this.profileNickname)
    this.$store.dispatch('getMyReview', this.profileNickname)
  }
}
</script>

<style>
#profile-box {
  width: 800px;
}
</style>