from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
def index(request):
    return render(request, 'main/main.html')
def test(request):
    return render(request, 'test/test.html')
