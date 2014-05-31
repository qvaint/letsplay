from django.contrib import admin
from myapp.models import Question, Result

# Register your models here.
admin.site.register(Question)
admin.site.register(Result)