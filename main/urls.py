
from django.conf.urls import include, url
from .views import index, test, check, history, endtest, testclinic, selectunit, unittest,mocktest, mocktestcheck, mockteststart, mocktestend
from django.urls import path
urlpatterns = [
    path(r'', index),
    path('history/', history),
    path('test/practice/', test),
    path('test/testclinic/', testclinic),
    path('test/check/', check),
    path('test/end/',endtest),
    path('test/selectunit/',selectunit),
    path('test/unittest/',unittest),
    path('test/mockteststart/',mockteststart),
    path('test/mocktest/<int:test_id>',mocktest),
    path('test/mockcheck/',mocktestcheck),
    path('test/mocktestend/<int:test_id>',mocktestend),
]
