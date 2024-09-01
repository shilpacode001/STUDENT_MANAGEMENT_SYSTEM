from django.contrib import admin
from .models import StudentMark


class StudentMarkAdmin(admin.ModelAdmin):
    pass



admin.site.register(StudentMark,StudentMarkAdmin)
