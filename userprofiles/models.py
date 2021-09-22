from django.db import models
from accounts.models import CustomUser, Teacher, Student
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    profile_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_img = models.ImageField(default='images/avatar1.png', upload_to='images/')


    def __str__(self):
        return f'{self.profile_user.username} UserProfile'
    

# @receiver(post_save, sender=CustomUser) #add this
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(profile_user=instance)


@receiver(post_save, sender=CustomUser)
def update_profile_signal(sender, instance, created, **kwargs):
    if created: 
        UserProfile.objects.create(profile_user=instance)
    instance.userprofile.save()
    

# @receiver(post_save, sender=CustomUser) #add this
# def save_user_profile(sender, instance, **kwargs):
# 	instance.userprofile.save()



# # Students Portal
# class StudentUserProfile(models.Model):
#     student_profile = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     student_profile_img = models.ImageField(default='images/avatar1.png')
#     comment = models.CharField(max_length=100)


# @receiver(post_save, sender=Student) #add this
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         StudentUserProfile.objects.create(is_student=instance)


# # Students Portal
# @receiver(post_save, sender=Student)
# def update_profile_signal(sender, instance, created, **kwargs):
#     if created: 
#         StudentUserProfile.objects.create(is_student=instance)
#     instance.is_student.save()


# # Students Portal 
# @receiver(post_save, sender=Student) #add this
# def save_user_profile(sender, instance, **kwargs):
# 	instance.is_student.save()
    




# # Teachers Portal
# class TeacherUserProfile(models.Model):
#     teachers_profile = models.ForeignKey(UserProfile,  on_delete=models.CASCADE)
#     hostel = models.CharField(max_length=100)

# @receiver(post_save, sender=Teacher) #add this
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         TeacherUserProfile.objects.create(is_teacher=instance)


# # Teachers Portal
# @receiver(post_save, sender=Teacher)
# def update_profile_signal(sender, instance, created, **kwargs):
#     if created: 
#         TeacherUserProfile.objects.create(is_teacher=instance)
#     instance.is_teacher.save()


# # Teachers Portal 
# @receiver(post_save, sender=Teacher) #add this
# def save_user_profile(sender, instance, **kwargs):
# 	instance.is_teacher.save()
    
