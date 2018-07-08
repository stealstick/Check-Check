from django.shortcuts import render
from .models import SolveLog, Timeline, Problem, Unit, Test
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




def selectunit(request):
    content = {
    'unit':Unit.objects.all(),
    }
    return render(request, 'test/selectunit.html', content)


def unittest(request):
    unitpk=request.GET['unit']
    unit=Unit.objects.get(pk=unitpk)
    for i in range(1,300):
        problems=Problem.objects.filter(unit=unit)
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
def mockteststart(request):
    test=Test.objects.create(user=request.user)

    return HttpResponseRedirect("/test/mocktest/"+str(test.pk))

def mocktest(request, test_id):
    test_id=test_id
    test= Test.objects.get(pk=test_id)
    if len(test.solve_problems.all())>=20:
        return HttpResponseRedirect("/test/mocktestend/"+str(test.pk))
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
        'test_id':test_id,
    }
    return render(request, 'test/mocktest.html', content)

def mocktestcheck(request):
    pk=request.POST['pk']
    answer=request.POST['answer']
    test_id=request.POST['test_id']
    problem=Problem.objects.get(pk=pk)
    if int(answer)==int(problem.answer):
        collect=True
        problem.solver.add(request.user)
        problem.no_solver.remove(request.user)
    else:
        collect=False
        problem.solver.remove(request.user)
        problem.no_solver.add(request.user)

    solve_problem=SolveLog.objects.create(problem=problem, user=request.user, answer=answer, collect=collect)
    test= Test.objects.get(pk=test_id)
    test.problems.add(problem)
    test.solve_problems.add(solve_problem)
    

    return HttpResponseRedirect("/test/mocktest/")

def mocktestend(request, test_id):
    test= Test.objects.get(pk=test_id)
    log=test.solve_problems.all()
    solve_count=len(test.solve_problems.all())
    solve_collect_count=0
    for i in test.solve_problems.all():
        if i.collect:
            solve_collect_count=solve_collect_count+1
    solve_not_collect_count=solve_count-solve_collect_count
    if solve_count !=0:
        collect_percent=round(solve_collect_count/solve_count*100)
    else:
        collect_percent=0

    content={
    'solve_count':solve_count,
    'solve_collect_count':solve_collect_count,
    'solve_not_collect_count':solve_not_collect_count,
    'collect_percent':collect_percent,
    'log':log,
    }
    return render(request, 'test/mockend.html', content)


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