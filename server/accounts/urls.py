from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('<int:user_pk>/update/', views.update, name='update'),
    path('<int:user_pk>/password/', views.password, name='password'),
    path('<str:username>/profile/', views.profile, name='profile'),
]