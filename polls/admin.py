from django.contrib import admin
from . models import Question , Choice
# Register your models here.
# Add Question to interface Admin

# class Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None , {"fields":["question_text"]}),
        ("Date description" , {"fields":["date_pub"]})
    ]
    inlines = [ChoiceInline]
    
    list_display = ["question_text" , "date_pub" , "was_published_recently"]
    
    # Add a filter
    list_filter = ["date_pub"]
    # Add search filter
    search_fields = ["question_text"]
    
admin.site.register(Question , QuestionAdmin)