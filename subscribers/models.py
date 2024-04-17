# subscribers/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
# class Subscriber(models.Model):
#     full_name = models.CharField(max_length=50)
#     phone_number = models.CharField(max_length=15)
#     email = models.EmailField(unique=True)
#     date_of_register = models.DateField(auto_now_add=True)
#     address = models.CharField(max_length= 250)

#     def __str__(self):
#         return self.full_name

class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='subscriber', null=True)
    date_of_register = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=250)
    amount_deposited = models.IntegerField()

    def __str__(self):
        return self.user.username if self.user else 'No User'

    @property
    def full_name(self):
        return self.user.get_full_name() if self.user else 'No User'

    @property
    def email(self):
        return self.user.email if self.user else 'No User Email'

    @property
    def phone_number(self):
        return self.user.phone_number if self.user else 'No User Phone Number'
    

class DaySaving(models.Model):
    subscriber = models.ForeignKey('Subscriber', on_delete=models.CASCADE)
    january_date = models.DateField(blank=True, null=True)
    february_date = models.DateField(blank=True, null=True)
    march_date = models.DateField(blank=True, null=True)
    april_date = models.DateField(blank=True, null=True)
    may_date = models.DateField(blank=True, null=True)
    june_date = models.DateField(blank=True, null=True)
    july_date = models.DateField(blank=True, null=True)
    august_date = models.DateField(blank=True, null=True)
    september_date = models.DateField(blank=True, null=True)
    october_date = models.DateField(blank=True, null=True)
    november_date = models.DateField(blank=True, null=True)
    december_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.subscriber.full_name} - {self.date}"
