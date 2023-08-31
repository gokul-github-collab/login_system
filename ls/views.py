from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView
from .models import *

class CustomLoginView(TemplateView):
    template_name = 'ls/login.html'

class StudentLoginView(LoginView):
    template_name = 'ls/student_login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.request.user.student.pk})

class FacultyLoginView(LoginView):
    template_name = 'ls/faculty_login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('faculty_detail', kwargs={'pk': self.request.user.faculty.pk})

class CustomLogoutView(LogoutView):
    next_page = '/'

class StudentView(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        projects = Project.objects.filter(student=student)
        context = {
            "student": student, "projects": projects
        }
        return render(request, "ls/student_detail.html", context)

class FacultyView(View):
    def get(self, request, pk):
        faculty = get_object_or_404(Faculty, pk=pk)
        projects = Project.objects.filter(faculty=faculty)
        context = {
            "faculty": faculty, "projects": projects
        }
        return render(request, "ls/faculty_detail.html", context)
