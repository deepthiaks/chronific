from django.contrib import admin
from .models import Hospital, Department, Specialist, FAQ


class HospitalList(admin.ModelAdmin):
    list_display = ('hospital_id', 'hospital_name', 'city')
    list_filter = ('hospital_id', 'hospital_name', 'city')
    search_fields = ('hospital_id', 'hospital_name')
    ordering = ['hospital_id','hospital_name']

class DepartmentList(admin.ModelAdmin):
    list_display = ('department_id','department_name')
    list_filter = ('department_id','department_name')
    search_fields = ('department_id','department_name')
    ordering = ['department_id','department_name']

class SpecialistList(admin.ModelAdmin):
    list_display = ('specialist_id','specialist_name','state')
    list_filter = ('specialist_id','specialist_name')
    search_fields = ('specialist_id','specialist_name','state')
    ordering = ['specialist_id','specialist_name']

class FAQList(admin.ModelAdmin):
    list_display = ('faq_id')
    list_filter = ('faq_id')
    search_fields=('faq_id')
    ordering = ['faq_id']

admin.site.register(Hospital, HospitalList)
admin.site.register(Department)
admin.site.register(Specialist)
admin.site.register(FAQ)

