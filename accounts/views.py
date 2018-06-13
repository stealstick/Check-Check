from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as _login, logout as _logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from django.http import HttpResponse, HttpResponseRedirect
def gologin(request):
    if request.user.is_active:
        return HttpResponseRedirect("/")
    else:
        return render(request, 'accounts/gologin.html')
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            _login(request, user)
            return redirect("/")
        else:
            pass
        return render(request, 'accounts/login.html', {'form': form})
    try:
        if request.GET['join']=="success": 
            return render(request, 'accounts/login.html', {'join':'success'})
    except:
        return render(request, 'accounts/login.html')
def index(request):
    return render(request, 'accounts/login.html', form)
def join(request):
    if request.method == "POST":
        username = request.POST['username']
        try:
            user=User.objects.get(username=username)
            content={
                'form': 'form'
            }
            return render(request, 'accounts/join.html', content)
        except:
            pass
        password = request.POST['password']
        useradd = User(username=username, password=password)
        useradd.set_password(password)
        useradd.save()
        return HttpResponseRedirect("/accounts/login/?join=success")
    return render(request, 'accounts/join.html')

def logout(request):
    _logout(request)
    return redirect("/")