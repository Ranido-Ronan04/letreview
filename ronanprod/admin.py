from django.contrib import admin
from .models import Participant, Reviewcenter, Enrolment, Payment, Reviewer
# Register your models here.
admin.site.register(Participant)
admin.site.register(Reviewcenter)
admin.site.register(Enrolment)
# admin.site.register(Result)
admin.site.register(Reviewer)
admin.site.register(Payment)