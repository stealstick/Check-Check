from django.db import models
from accounts.models import User
ANSWER_CHOICE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

class Unit(models.Model):
    unit= models.CharField(max_length=200, help_text="단원")
    def __str__(self):
        return self.unit
class Problem(models.Model):
    title = models.CharField(max_length=100, help_text="문제")
    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(blank=True)
    ex1 = models.CharField(max_length=200, help_text="보기1")
    ex2 = models.CharField(max_length=200, help_text="보기2")
    ex3 = models.CharField(max_length=200, help_text="보기3")
    ex4 = models.CharField(max_length=200, help_text="보기4")
    ex5 = models.CharField(max_length=200, help_text="보기5")
    answer = models.PositiveIntegerField(default=1, help_text="정답", choices=ANSWER_CHOICE)
    solver = models.ManyToManyField(User, related_name="solver", blank=True)
    no_solver = models.ManyToManyField(User, related_name="nosolver", blank=True)
    def __str__(self):
        return self.title

class SolveLog(models.Model):
    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    answer = models.PositiveIntegerField(default=1, help_text="입력한 정답", choices=ANSWER_CHOICE)
    collect = models.BooleanField(default=False, help_text="맞았는지")
    time =  models.DateTimeField()
    def __str__(self):
        return self.user.username+" "+self.problem.title
