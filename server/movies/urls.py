from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_index, name='movie_index'),
    path('recommended/', views.movie_recommended, name='movie_recommended'),
    path('<int:movie_pk>/movie_detail/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/movie_create/', views.movie_create, name='movie_create'),
    path('<int:movie_pk>/movie_update/', views.movie_update, name='movie_update'),
    path('<int:movie_pk>/movie_delete/', views.movie_delete, name='movie_delete'),
    path('<int:movie_pk>/movie_like/', views.movie_like, name='movie_like'),
    path('<int:movie_pk>/', views.review_detail, name='review_detail'),
    path('<int:movie_pk>/review_create/', views.review_create, name='review_create'),
    path('<int:movie_pk>/movie_update/', views.review_update, name='review_update'),
    path('<int:movie_pk>/movie_delete/', views.review_delete, name='review_delete'),
    path('<int:movie_pk>/movie_like/', views.review_like, name='review_like'),
    path('<int:movie_pk>/movie_update/', views.comment_create, name='comment_create'),
    path('<int:movie_pk>/movie_delete/', views.comment_delete, name='comment_delete'),
    path('<int:movie_pk>/follow/', views.follow, name='follow'),
]
