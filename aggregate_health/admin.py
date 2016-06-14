from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Patient)
admin.site.register(PrimaryCareProvider)
admin.site.register(VisitTypes)
admin.site.register(Encounter)
admin.site.register(Condition)
admin.site.register(ProblemList)