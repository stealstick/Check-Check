from django.conf.urls import include, url
from . import views
from main.views import test
from django.urls import path
urlpatterns = [
    url(r'login/', views.login),
    url(r'join/', views.join),
]