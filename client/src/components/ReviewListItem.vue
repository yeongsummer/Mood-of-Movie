<template>
  <div id="review-list-item">
    <div class="review_info">
      <div class="movie_title">
        {{review.movie.title}}
      </div>
      <div class="review__info-title">
        {{ review.title }}
      </div>
      <div>
        <v-rating
          class="d-inline"
          color="yellow darken-3"
          background-color="grey darken-1"
          empty-icon="$ratingFull"
          half-increments
          readonly
          hover
          size="15"
          :value="review.rank/2"
        ></v-rating>
        <span>{{review.rank}} / 10</span>
      </div>
      <div class="review_info--desc">
        {{ review.content }}
      </div>
      <div class="review_info--date">
        {{ review.user.nickname }} |
        {{ review.created_at | moment('YYYY-MM-DD hh:mm') }}
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  },
}
</script>

<style>
#review-list-item {
  display: flex;
  margin: 24px;
  border: 2px solid #ebebec;
  border-radius: 4px;
  padding: 15px 8px;
  color:#484848;

}

#review-list-item:hover {
  cursor: pointer;
  opacity: 0.5;
  transition: 0.2s;
  transform: translateY(-2px);
}
.movie_title {
  display: inline;
  margin: 10px;
  background-color: #f8e6ab;
  border-radius: 5px;
  padding: 6px 4px 4px 4px;
}
.review__info-title {
  margin-top: 10px;
  margin-left: 10px;
  font-weight: bold;
  font-size: 1.5rem;
}

.review_info--desc {
  margin-top: 10px;
  margin-left: 10px;
  display: -webkit-box; 
  -webkit-box-orient: vertical; 
  word-wrap: break-word; 
  text-overflow: ellipsis; 
  overflow: hidden;
  -webkit-line-clamp: 3;
}

.review_info--date {
  font-size: 0.9rem;
  margin-top: 10px;
  margin-left: 10px;
}
</style>