from django.contrib import admin
from .models import Let, Center, Exam, Feedback
# Register your models here.
admin.site.register(Let)
admin.site.register(Center)
admin.site.register(Exam)
# admin.site.register(Result)
admin.site.register(Feedback)