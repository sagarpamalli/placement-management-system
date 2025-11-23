from django.urls import path
from . import views

urlpatterns = [
    path('student/register/', views.student_register, name='student_register'),
    path('company/register/', views.company_register, name='company_register'),
    path('logout/', views.custom_logout, name='logout'),
    path('contact-admin/', views.contact_admin, name='contact_admin'),
]