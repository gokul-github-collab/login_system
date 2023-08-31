from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('login/student/', views.StudentLoginView.as_view(), name='student_login'),
    path('login/faculty/', views.FacultyLoginView.as_view(), name='faculty_login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('student/<int:pk>/', views.StudentView.as_view(), name='student_detail'),
    path('faculty/<int:pk>/', views.FacultyView.as_view(), name='faculty_detail'),
]
