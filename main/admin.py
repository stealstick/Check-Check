from django.contrib import admin
from .models import Problem, Unit, SolveLog
# Register your models here.
admin.site.register(Problem)
admin.site.register(Unit)
admin.site.register(SolveLog)