from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("create/", views.create_user, name="create_user"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("users_home/", views.users_home, name="users_home"),
]