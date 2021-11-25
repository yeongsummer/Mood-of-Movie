from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('password/', views.password, name='password'),
    path('<nickname>/follow/', views.follow, name="follow"),
    path('api-token-auth/', obtain_jwt_token),
    path('user/', views.get_user),
    path('<nickname>/get_followers/', views.get_followers),
    path('<nickname>/get_followings/', views.get_followings),
    path('<nickname>/get_like_movies/', views.get_like_movies),
    # path('<int:user_pk>/user_profile_update_delete/', views.user_profile_update_delete),
    path('<nickname>/review_list/', views.get_review),
    path('<nickname>/upload_img/', views.upload_img),
]