from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=20)
    program = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)


    def __str__(self):
        return self.name


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='faculty_images/', blank=True, null=True)
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='module_images/', blank=True, null=True)
    faculty_rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
