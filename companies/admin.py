from django.contrib import admin
from .models import Company, Vacancy, Response

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'full_name', 'phone_number', 'industry', 'created_at')
    search_fields = ('company_name', 'full_name', 'phone_number', 'industry')

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'specialization', 'city', 'hiring_plan', 'salary_min', 'salary_max')
    search_fields = ('job_title', 'specialization', 'city')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position', 'experience')
    search_fields = ('full_name', 'position', 'experience')
