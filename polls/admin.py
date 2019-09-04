from django.contrib import admin
from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    """Link Choice with Question Model Admin."""

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """Customize Question Model Admin."""

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
