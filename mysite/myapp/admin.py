from django.contrib import admin
from myapp.models import Question, Result

class QuestionAdmin(admin.ModelAdmin):
  list_display = ('platform_choice', 'platform_name', 'game_preference')
  list_filter = ['platform_choice', 'platform_name', 'game_preference']
  search_fields = ['platform_choice', 'platform_name', 'game_preference']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Result)