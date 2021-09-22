from django.shortcuts import render
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.views import generic
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

# Create your views here.

@login_required
def user_profile(request, user_id):
    if request.method == 'POST': 
        user_obj = CustomUser.objects.get(id=user_id)
        user_profile_obj = UserProfile.objects.get(id=user_id)
        user_img = request.FILES['user_img']
        fs_handle = FileSystemStorage()
        img_name = 'images/user_{0}'.format(user_id)
        if fs_handle.exists(img_name):
            fs_handle.delete(img_name)
        fs_handle.save(img_name, user_img)
        user_profile_obj.profile_img = img_name
        user_profile_obj.save()
        user_profile_obj.refresh_from_db()
        return render(request, 'my_profile.html', {'my_profile': user_profile_obj})
    
    if (request.user.is_authenticated and request.user.id == user_id):
        user_obj = CustomUser.objects.get(id=user_id)
        user_profile = UserProfile.objects.get(id=user_id)
        return render(request, 'my_profile.html', {'my_profile': user_profile}) 


# """
# Teachers Profile Page
# """
# @login_required
# def teacher_profile(request, user_id):
#     if request.method == 'POST': 
#         teacher_obj = CustomUser.objects.get(id=user_id)
#         teacher_profile_obj = TeacherUserProfile.objects.get(id=user_id)
#         teacher_img = request.FILES['user_img']
#         fs_handle = FileSystemStorage()
#         img_name = 'images/user_{0}'.format(user_id)
#         if fs_handle.exists(img_name):
#             fs_handle.delete(img_name)
#         fs_handle.save(img_name, user_img)
#         teacher_profile_obj.profile_img = img_name
#         teacher_profile_obj.save()
#         teacher_profile_obj.refresh_from_db()
#         return render(request, 'teacher_profile.html', {'teacher_profile': teacher_profile_obj})
    
#     if (request.user.is_authenticated and request.user.id == user_id):
#         teacher_obj = CustomUser.objects.get(id=user_id)
#         teacher_profile = TeacherUserProfile.objects.get(id=user_id)
#         return render(request, 'teacher_profile.html', {'teacher_profile': teacher_profile}) 




# """
# Teachers Profile Page
# """
# @login_required
# def student_profile(request, user_id):
#     if request.method == 'POST': 
#         student_obj = CustomUser.objects.get(id=user_id)
#         student_profile_obj = StudentUserProfile.objects.get(id=user_id)
#         student_img = request.FILES['user_img']
#         fs_handle = FileSystemStorage()
#         img_name = 'images/user_{0}'.format(user_id)
#         if fs_handle.exists(img_name):
#             fs_handle.delete(img_name)
#         fs_handle.save(img_name, user_img)
#         student_profile_obj.profile_img = img_name
#         student_profile_obj.save()
#         student_profile_obj.refresh_from_db()
#         return render(request, 'student_profile.html', {'student_profile': student_profile_obj})
    
#     if (request.user.is_authenticated and request.user.id == user_id):
#         student_obj = CustomUser.objects.get(id=user_id)
#         student_profile = StudentUserProfile.objects.get(id=user_id)
#         return render(request, 'student_profile.html', {'student_profile': student_profile}) 





"""
Edit Teachers Profile Page
"""
class EditTeachersProfilePageView(generic.UpdateView):
    model = UserProfile
    template_name = 'edit_teachers_profile.html'
    fields = ["username", "phone_number","email", ]
    success_url = reverse_lazy('teacher_page')




"""
Edit Student Profile Page
"""
class EditStudentsProfilePageView(generic.UpdateView):
    model = UserProfile
    template_name = 'edit_students_profile.html'
    fields = ["username", "phone_number","email", ]
    success_url = reverse_lazy('student_page')

