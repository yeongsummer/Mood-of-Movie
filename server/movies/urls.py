from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('movie_recommend/', views.movie_recommend),
    path('movie_video/<int:movie_pk>/', views.getMovieVideoKey),
    # path('<int:movie_pk>/', views.movie_detail),
    path('review_list/<int:movie_pk>/', views.review_list_create),
    path('review/<int:review_pk>/', views.review_detail_update_delete),
    path('comment_list/<int:review_pk>/', views.comment_list_create),
    path('comment/<int:comment_pk>/', views.comment_detail_update_delete),

]