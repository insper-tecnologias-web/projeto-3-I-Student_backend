from django.contrib import admin
from .models import Course, Subject, Summary

# Register your models here.
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Summary)