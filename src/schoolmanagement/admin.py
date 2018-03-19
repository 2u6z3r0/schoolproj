from django.contrib import admin

# Register your models here.
from .models import Student, School

class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'registerNum', 'dob', 'gender', 'admissionDate', 'caste']
    list_filter = ['name', 'gender', 'admissionDate', 'caste']
    search_fields = ['name', 'registerNum', 'caste', 'adharcardNum']
    class Meta:
        model = Student

class SchoolModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'schoolCode', 'village', 'taluk', 'dist']
    list_filter = ['name', 'schoolCode', 'village', 'taluk', 'dist']
    search_fields = ['name', 'schoolCode', 'village', 'taluk', 'dist']

    class Meta:
        model = School

admin.site.register(School, SchoolModelAdmin,)
admin.site.register(Student, StudentModelAdmin,)