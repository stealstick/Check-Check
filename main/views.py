from django.shortcuts import render
from .models import SolveLog, Timeline
from django.http import HttpResponse, HttpResponseRedirect
def index(request):
    if not request.user.is_active:
        return render(request, 'accounts/gologin.html')
        
    solve_count_query=SolveLog.objects.filter(user=request.user)
    solve_count=len(solve_count_query)
    solve_collect_count_query=SolveLog.objects.filter(user=request.user, collect=True)
    solve_collect_count=len(solve_collect_count_query)
    solve_not_collect_count=solve_count-solve_collect_count
    if solve_count !=0:
        collect_percent=round(solve_collect_count/solve_count*100)
    else:
        collect_percent=0

    timeline=Timeline.objects.all()

    content={
    'solve_count':solve_count,
    'solve_collect_count':solve_collect_count,
    'solve_not_collect_count':solve_not_collect_count,
    'collect_percent':collect_percent,
    'timeline':timeline

    }
    return render(request, 'main/main.html', content)
def test(request):
    return render(request, 'test/test.html')
