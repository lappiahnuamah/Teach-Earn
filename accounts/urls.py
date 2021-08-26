from django.urls import path
from .views import register, HomeView, student_register, verification_sent, teacher_register, login_view, StudentProfileView, TeacherProfileView

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('register/', register, name='register'),
  path('register/login/', login_view, name='login_view'),
  path('student_register/', student_register.as_view(), name='student_register'),
  path('teacher_register/', teacher_register.as_view(), name='teacher_register'),
  path('verification/', verification_sent.as_view(), name='verify_account'),
  path('student/profile/', StudentProfileView.as_view(), name='student_page'),
  path('teacher/profile/', TeacherProfileView.as_view(), name='teacher_page'),
]