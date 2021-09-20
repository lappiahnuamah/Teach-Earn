from .models import CustomUser

new_cred = CustomUser.objects.create(username="John", is_student=True)
def redirect_to_profile_page(user):
    if user.is_student == True:
        return 'student_page'
    else:
        return 'teacher_page'