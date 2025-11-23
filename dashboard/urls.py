from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('company/', views.company_dashboard, name='company_dashboard'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
]