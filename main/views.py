from django.shortcuts import render
from .models import SolveLog, Timeline, Problem
from django.http import HttpResponse, HttpResponseRedirect
from random import shuffle

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
    timeline=timeline.order_by('-time')
    content={
    'solve_count':solve_count,
    'solve_collect_count':solve_collect_count,
    'solve_not_collect_count':solve_not_collect_count,
    'collect_percent':collect_percent,
    'timeline':timeline,
    }
    return render(request, 'main/main.html', content)

def history(request):
    if not request.user.is_active:
        return render(request, 'accounts/gologin.html')
        
    solvelogs=SolveLog.objects.filter(user=request.user)
    solvelogs=solvelogs.order_by('-time')
    content={
    'solvelogs':solvelogs
    }
    return render(request, 'main/history.html', content)    


def test(request):
    for i in range(1,300):
        problems=Problem.objects.all()
        problems_random=list(problems)
        shuffle(problems_random)
        problem=problems_random[0]
        if request.user in problem.solver.all():
            pass
        else:
            break
    content={
        'problem':problem,
    }
    return render(request, 'test/test.html', content)

def testclinic(request):
    problems=Problem.objects.filter(no_solver=request.user)
    problems_random=list(problems)
    shuffle(problems_random)
    if not len(problems):
        return HttpResponseRedirect("/")
    print(len(problems))
    problem=problems_random[0]
    content={
        'problem':problem,
    }
    return render(request, 'test/testclinic.html', content)



def check(request):
    pk=request.POST['pk']
    answer=request.POST['answer']
    problem=Problem.objects.get(pk=pk)
    if int(answer)==int(problem.answer):
        collect=True
        problem.solver.add(request.user)
        problem.no_solver.remove(request.user)
    else:
        collect=False
        problem.solver.remove(request.user)
        problem.no_solver.add(request.user)

    SolveLog.objects.create(problem=problem, user=request.user, answer=answer, collect=collect)

    return HttpResponseRedirect("/test/practice/")

def endtest(request):
    Timeline.objects.create(title=request.user.username, user=request.user, icon="insert_chart", content="테스트를 마치셨습니다.")

    return HttpResponseRedirect("/")