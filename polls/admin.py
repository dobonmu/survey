from django.contrib import admin
from .models import Question, Choice,Open_answer

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Open_answer)
# Register your models here.
