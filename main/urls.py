
from django.conf.urls import include, url
from .views import index, test
from django.urls import path
urlpatterns = [
    path(r'', index),
    path('test/', test),
]
