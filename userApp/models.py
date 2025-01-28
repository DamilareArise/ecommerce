from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    
    gend = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]
    
    
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profilePictures/', null=True)
    gender = models.CharField(choices=gend, max_length=50, null=True),
    country = models.CharField(max_length=50, null=True)
    date_of_birth = models.CharField(max_length=11, null=True)
    
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()