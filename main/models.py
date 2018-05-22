from django.db import models
from accounts.models import User

UNIT_CHOICE = (
        (1, '생활과 윤리의 의의 '),
        (2, '생명.성 윤리'),
        (3, '가족 윤리'),
        (4, '과학.생태.정보 윤리'),
        (5, '사회 정의'),
        (6, '직업윤리'),
        (7, '문화와 윤리'),
        (8, '평화와 윤리'),
    )
ANSWER_CHOICE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
class Problem(models.Model):
    title = models.CharField(max_length=100, help_text="문제 이름")
    unit = models.CharField(max_length=30, help_text="단원", choices=UNIT_CHOICE)
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
