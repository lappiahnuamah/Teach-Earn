from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import  settings

urlpatterns = [
    path('<int:user_id>/', views.user_profile, name='profile'),
    # path('teacher/<int:user_id>/', views.teacher_profile, name='teacher_profile'),
    # path('student/<int:user_id>/', views.student_profile, name='student_profile'),
]
