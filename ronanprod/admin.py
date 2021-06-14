from django.contrib import admin
from .models import Participant, ReviewCenter, Enrollment, Feedback, Schedule
# Register your models here.
admin.site.register(Participant)
admin.site.register(ReviewCenter)
admin.site.register(Enrollment)
# admin.site.register(Result)
admin.site.register(Feedback)
admin.site.register(Schedule)