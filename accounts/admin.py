from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Student, Company, Job, Application

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'user_type', 'first_name', 'last_name', 'is_staff']
    list_filter = ['user_type', 'is_staff', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('user_type', 'phone')}),
    )

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'enrollment_number', 'department', 'semester', 'cgpa']
    search_fields = ['user__first_name', 'user__last_name', 'enrollment_number']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'contact_person', 'contact_email', 'website']
    search_fields = ['company_name', 'contact_person']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'job_type', 'application_deadline', 'is_active']
    list_filter = ['job_type', 'is_active', 'posted_date']
    search_fields = ['title', 'company__company_name']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['student', 'job', 'applied_date', 'status']
    list_filter = ['status', 'applied_date']
    search_fields = ['student__user__first_name', 'student__user__last_name', 'job__title']