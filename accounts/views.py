from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm, CompanyRegistrationForm
from .models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_dashboard')
    else:
        form = StudentRegistrationForm()
    return render(request, 'accounts/student_register.html', {'form': form})

def company_register(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('company_dashboard')
    else:
        form = CompanyRegistrationForm()
    return render(request, 'accounts/company_register.html', {'form': form})

@login_required
def custom_logout(request):
    logout(request)
    return redirect('index')

def contact_admin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        user_type = request.POST.get('user_type')
        
        # Send email to admin (you'll need to configure email settings)
        try:
            send_mail(
                f'Placement System: {subject}',
                f'''
                Name: {name}
                Email: {email}
                User Type: {user_type}
                
                Message:
                {message}
                ''',
                settings.DEFAULT_FROM_EMAIL,
                ['admin@college.edu'],  # Admin email
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent to the admin successfully!')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again.')
        
        return redirect('contact_admin')
    
    return render(request, 'accounts/contact_admin.html')
