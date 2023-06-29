from django.db import models
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

def profile_images_upload_path(instance, file_name):
    return f"{instance.user_slug}/User/Profile/profile_picture/{file_name}"


def profile_display_images_upload_path(instance, file_name):
    return f"{instance.user.user_slug}/User/Profile/profile_display/{file_name}"


class User(AbstractUser):
    visitor_check = models.BooleanField(default=False)
    ticket_service = models.BooleanField(default=False)
    restaurant_service = models.BooleanField(default=False)
    apartment_service = models.BooleanField(default=False)
    hotel_service = models.BooleanField(default=False)
    is_reception = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_office = models.BooleanField(default=False)
    user_slug = models.SlugField(null=True)
    profile_pic = models.ImageField(upload_to=profile_images_upload_path, null=True)
    

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class Vendor(models.Model):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Reception(models.Model):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)
    def __str__(self):
            return self.user.username

class Office(models.Model):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ProfileDisplayImages(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    display_images = models.ImageField(upload_to=profile_display_images_upload_path, null=True)

    def __str__(self):
        return self.user.user_slug

    