from django.contrib import admin
from.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'roll', 'name', 'marks', 'image']
admin.site.register(Student, StudentAdmin)

