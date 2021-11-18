from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<int:user_pk>/password/', views.password, name='password'),
    path('<int:user_pk>/follow/', views.follow, name="follow"),
    path('api-token-auth/', obtain_jwt_token),
]