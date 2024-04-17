from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# class InactiveManager(models.Manager):
   
#     def get_queryset(self):
#         return super().get_queryset().filter(is_active=False)

# class ActiveManager(models.Manager):

#     def get_queryset(self):
#         return super().get_queryset().filter(is_active=True)


class User(AbstractUser):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=19, unique=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to="user_profile_picture", default="avatar.svg")
    phone_number = PhoneNumberField()
    is_active = models.BooleanField(default=True)
    is_admin =  models.BooleanField(default=False)
    amount_deposited = models.IntegerField(default=0)



    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

 
    
    def __str__(self):
        return self.username
    
    
    @property
    def image_URL(self):
        try:
            url= self.profile_picture.url
        except:
            url= ''
        return url
    

