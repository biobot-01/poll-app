from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    """Customize Question Model Admin."""

    fields = ['pub_date', 'question_text']


admin.site.register(Question, QuestionAdmin)
