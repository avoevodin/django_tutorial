from django.contrib import admin
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'id', 'question_text', 'pub_date',
    ]
    readonly_fields = [
        'id'
    ]
    list_display = [
        'id', 'question_text', 'pub_date', 'was_published_recently',
    ]
    list_display_links = [
        'id', 'question_text'
    ]
    search_fields = [
        '^question_text'
    ]
    list_filter = [
        'pub_date'
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
