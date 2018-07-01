
from django.conf.urls import include, url
from .views import index, test, check, history, endtest, testclinic
from django.urls import path
urlpatterns = [
    path(r'', index),
    path('history/', history),
    path('test/practice/', test),
    path('test/testclinic/', testclinic),
    path('test/check/', check),
    path('test/end/',endtest)
]
