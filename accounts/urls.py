from django.urls import path
from rest_framework.routers import SimpleRouter

from accounts.views import ListCreateUserAPI


app_name = 'accounts'

urlpatterns = [
    path("", ListCreateUserAPI.as_view())
]