from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    """Customize Question Model Admin."""

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)
