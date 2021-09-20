from django.db import models
from accounts.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    profile_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_img = models.ImageField(default='images/avatar1.png')

@receiver(post_save, sender=CustomUser)
def update_profile_signal(sender, instance, created, **kwargs):
    if created: 
        UserProfile.objects.create(profile_user=instance)
    instance.userprofile.save()
    

@receiver(post_save, sender=CustomUser) #add this
def save_user_profile(sender, instance, **kwargs):
	instance.userprofile.save()
