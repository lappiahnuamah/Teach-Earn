from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import CustomUser, Student, Teacher
from video_content.models import Video

admin.site.register(CustomUser)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'comment']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']


admin.site.register(Student, StudentAdmin)

admin.site.register(Teacher, TeacherAdmin)

admin.site.register(Video)