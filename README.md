# Placement Management System

A comprehensive Django-based web application designed to streamline campus placement processes, connecting students with companies through an interactive platform with role-based dashboards, job management, and real-time analytics.

## 🚀 Features
👨‍🎓 **Student Portal** - Register, upload resumes, browse jobs, and track applications.
🏢 **Company Portal** - Register companies, post jobs, and manage candidate applications.
👨‍💼 **Admin Dashboard** - Monitor system analytics, manage users, and oversee placements.
📊 **Interactive Dashboards** - Real-time statistics and performance metrics for all user types.
📄 **Resume Management** - Upload and manage resumes with secure file handling.
🔐 **Role-based Authentication** - Secure login system for students, companies, and admins.
💼 **Job Application System** - One-click job applications with status tracking.
📈 **Analytics & Reporting** - Comprehensive insights into placement activities.

## 🧰 Tech Stack
### Languages & Frameworks
- **Python**
- **Django**
- **HTML/CSS**
- **JavaScript**
- **Bootstrap**
- **SQLite**

### Key Libraries
- **Django 4.2** - Web framework
- **Pillow** - Image processing
- **Bootstrap 5** - Frontend framework

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/sagarpamalli/placement-management-system.git
cd placement-management-system
2. Install dependencies
bash
pip install -r requirements.txt
3. Run migrations
bash
python manage.py makemigrations
python manage.py migrate
4. Create admin user
bash
python manage.py createsuperuser
5. Run development server
bash
python manage.py runserver
6. Open in browser
The application will open at http://localhost:8000

Access Points
Main Application: http://localhost:8000/

Student Registration: http://localhost:8000/accounts/student/register/

Company Registration: http://localhost:8000/accounts/company/register/

Admin Login: http://localhost:8000/admin-login/

Default Admin Credentials
text
Username: admin
Password: admin123
Email: admin@college.edu
About
A complete placement management solution built with Django that digitalizes the entire campus placement process, providing dedicated interfaces for students, companies, and placement officers.
