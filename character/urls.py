from django.urls import path
from .views import home, About

urlpatterns = [
    path("", home.as_view(), name="home"),
    path("about/", About.as_view(), name="about"),
]
