from django.contrib import admin
from .models import Problem, Unit, SolveLog, Timeline, Test
# Register your models here.
admin.site.register(Problem)
admin.site.register(Unit)
admin.site.register(Timeline)
admin.site.register(SolveLog)

admin.site.register(Test)