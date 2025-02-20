from django.urls import path
from .views import registration, home, user_login, user_logout, delete_user


urlpatterns = [
    path('', registration, name="registration"),
    path('dashboard',home, name="dashboard"),
    path("logout",user_logout, name="logout" ),
    path("login", user_login, name="login"),
    path('delete/<int:pk>',delete_user, name="delete_user" )
]
