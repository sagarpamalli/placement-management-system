from django import forms
from accounts.models import Job, Student
from django.utils import timezone

class JobForm(forms.ModelForm):
    application_deadline = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=timezone.now().date()
    )
    
    class Meta:
        model = Job
        fields = ['title', 'description', 'requirements', 'location', 
                 'salary', 'job_type', 'application_deadline']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'requirements': forms.Textarea(attrs={'rows': 4}),
        }

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['resume']