from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

    fields = [
        'id', 'question', 'choice_text', 'votes',
    ]

    readonly_fields = [
        'id',
    ]
    list_display = [
        'id', 'question', 'choice_text', 'votes',
    ]
    list_display_links = [
        'id', 'choice_text',
    ]
    search_fields = [
        'choice_text',
    ]
    list_filter = [
        'question__question_text',
        'pub_date',
    ]


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['id', 'question_text']}),
        (
            _('Date information'),
            {'fields': ['pub_date']}
        )
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
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
