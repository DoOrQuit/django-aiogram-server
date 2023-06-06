from django.urls import path

from accounts.views import UserListCreateAPI, UserDetailAPI, login_view, registration_view, logout_view

app_name = 'accounts'

urlpatterns = [
    path("api/v1/users/", UserListCreateAPI.as_view()),
    path("api/v1/users/<email>", UserDetailAPI.as_view()),
    path("login/", login_view, name="login"),
    path("register/", registration_view, name="registration"),
    path("logout/", logout_view, name="logout")
]
