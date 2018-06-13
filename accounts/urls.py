from django.conf.urls import include, url
from . import views
from main.views import test
from django.urls import path
urlpatterns = [
    url(r'/login/', views.login,name='login'),
    url(r'/gologin/', views.gologin),
    url(r'join/', views.join),
    url(r'logout/', views.logout),
]