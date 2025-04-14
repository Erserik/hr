from django.contrib import admin
from .models import UserRegistration, UserResume

@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'created_at')
    search_fields = ('full_name', 'phone_number')

@admin.register(UserResume)
class UserResumeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'position',
        'specialization',
        'work_format',
        'expected_salary',
        'experience'
    )
    search_fields = ('full_name', 'position', 'specialization', 'experience')
