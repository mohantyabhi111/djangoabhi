from django.contrib import admin

from .models import Choice,Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['text']}),
        ('Date information', {'fields': ['publishing_date']}),
    ]
    list_display = ('text', 'publishing_date', 'was_published_recently')
    list_filter = ['publishing_date']
    search_fields = ['text']
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
