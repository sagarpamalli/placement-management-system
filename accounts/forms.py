from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Company

class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    enrollment_number = forms.CharField(max_length=20, required=True)
    department = forms.CharField(max_length=100, required=True)
    semester = forms.IntegerField(min_value=1, max_value=8, required=True)
    cgpa = forms.DecimalField(max_digits=3, decimal_places=2, required=True)
    skills = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 
                 'enrollment_number', 'department', 'semester', 'cgpa', 'skills',
                 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'student'
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        
        if commit:
            user.save()
            student = Student.objects.create(
                user=user,
                enrollment_number=self.cleaned_data['enrollment_number'],
                department=self.cleaned_data['department'],
                semester=self.cleaned_data['semester'],
                cgpa=self.cleaned_data['cgpa'],
                skills=self.cleaned_data['skills']
            )
        return user

class CompanyRegistrationForm(UserCreationForm):
    company_name = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)
    website = forms.URLField(required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    contact_person = forms.CharField(max_length=100, required=True)
    contact_email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'company_name', 'description', 'website', 
                 'address', 'contact_person', 'contact_email', 'phone',
                 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'company'
        user.email = self.cleaned_data['contact_email']
        user.phone = self.cleaned_data['phone']
        user.first_name = self.cleaned_data['contact_person']
        
        if commit:
            user.save()
            company = Company.objects.create(
                user=user,
                company_name=self.cleaned_data['company_name'],
                description=self.cleaned_data['description'],
                website=self.cleaned_data['website'],
                address=self.cleaned_data['address'],
                contact_person=self.cleaned_data['contact_person'],
                contact_email=self.cleaned_data['contact_email']
            )
        return user