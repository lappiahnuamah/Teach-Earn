from django.shortcuts import render
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from .models import UserProfile 
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