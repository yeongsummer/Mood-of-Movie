from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list_create),
    path('<int:movie_pk>/', views.movie_detail_update_delete),
    path('review/', views.review_detail_update_delete),
    path('review/<int:review_pk>/', views.review_detail_update_delete),
    path('comment/', views.comment_list_create),
    path('comment/<int:comment_pk>/', views.comment_detail_update_delete),

]
