from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from accounts.models import Student, Company, Job, Application
from .forms import JobForm, ResumeForm

@login_required
def dashboard(request):
    user_type = request.user.user_type
    if user_type == 'student':
        return redirect('student_dashboard')
    elif user_type == 'company':
        return redirect('company_dashboard')
    elif user_type == 'admin':
        return redirect('admin_dashboard')
    return redirect('index')

@login_required
def student_dashboard(request):
    student = get_object_or_404(Student, user=request.user)
    jobs = Job.objects.filter(is_active=True, application_deadline__gte=timezone.now().date())
    applications = Application.objects.filter(student=student)
    applied_job_ids = applications.values_list('job_id', flat=True)
    
    if request.method == 'POST' and 'resume' in request.FILES:
        form = ResumeForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_dashboard')
    else:
        form = ResumeForm(instance=student)
    
    context = {
        'student': student,
        'jobs': jobs,
        'applications': applications,
        'applied_job_ids': list(applied_job_ids),
        'form': form,
    }
    return render(request, 'dashboard/student_dashboard.html', context)

@login_required
def apply_job(request, job_id):
    if request.user.user_type != 'student':
        return redirect('dashboard')
    
    student = get_object_or_404(Student, user=request.user)
    job = get_object_or_404(Job, id=job_id, is_active=True)
    
    # Check if already applied
    if Application.objects.filter(student=student, job=job).exists():
        return redirect('student_dashboard')
    
    # Check if resume is uploaded
    if not student.resume:
        return redirect('student_dashboard')
    
    # Create application
    Application.objects.create(student=student, job=job)
    return redirect('student_dashboard')

@login_required
def company_dashboard(request):
    company = get_object_or_404(Company, user=request.user)
    jobs = Job.objects.filter(company=company)
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = company
            job.save()
            return redirect('company_dashboard')
    else:
        form = JobForm()
    
    # Get applications for company's jobs
    applications = Application.objects.filter(job__company=company).select_related('student', 'job')
    
    context = {
        'company': company,
        'jobs': jobs,
        'applications': applications,
        'form': form,
    }
    return render(request, 'dashboard/company_dashboard.html', context)

@login_required
def admin_dashboard(request):
    if request.user.user_type != 'admin':
        return redirect('dashboard')
    
    total_students = Student.objects.count()
    total_companies = Company.objects.count()
    total_jobs = Job.objects.count()
    total_applications = Application.objects.count()
    
    companies = Company.objects.all()
    jobs = Job.objects.select_related('company').all()
    applications = Application.objects.select_related('student', 'job').all()
    
    context = {
        'total_students': total_students,
        'total_companies': total_companies,
        'total_jobs': total_jobs,
        'total_applications': total_applications,
        'companies': companies,
        'jobs': jobs,
        'applications': applications,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)
