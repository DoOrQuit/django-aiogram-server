from django.urls import path

from core.views import home_page_view, redirect_view

app_name = 'core'

urlpatterns = [
    path("home/", home_page_view, name="home"),
]
