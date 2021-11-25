from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.popular_movie_list),
    path('all_movie/',views.movie_list),
    path('movie_detail/<movie_title>/', views.movie_detail),
    path('movie_recommend/<movie_title>/', views.movie_recommend),
    path('review_search/<search>/', views.review_search),
    path('movie_video/<int:movie_pk>/', views.getMovieVideoKey),
    path('review_list/', views.review_list_all),
    path('review_list/<int:movie_pk>/', views.review_list_create),
    path('review/<int:review_pk>/', views.review_detail_update_delete),
    path('comment_list/<int:review_pk>/', views.comment_list_create),
    path('comment/<int:comment_pk>/', views.comment_detail_delete),
    path('movie_like/<int:movie_pk>/', views.movie_like),
    path('review_like/<int:review_pk>/', views.review_like),

]