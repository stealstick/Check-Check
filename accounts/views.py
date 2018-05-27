from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
def login(request):
    return render(request, 'accounts/login.html')
def join(request):
    return render(request, 'accounts/join.html')