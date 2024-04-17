from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Subscriber, DaySaving

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'middle_name', 'username', 'email', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control data-list'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class SubscriberForm(forms.ModelForm):
    date_of_register = forms.DateField(widget=forms.HiddenInput(), required=False)
    address = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    amount_deposited = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Subscriber
        fields = ['address', 'amount_deposited']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'amount_deposited': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def save(self, user, commit=True):
        subscriber = super().save(commit=False)
        subscriber.user = user
        subscriber.save()
        return subscriber

class DaySavingForm(forms.ModelForm):
    class Meta:
        model = DaySaving
        fields = ['january_date', 'february_date', 'march_date', 'april_date', 'may_date', 'june_date',
                  'july_date', 'august_date', 'september_date', 'october_date', 'november_date', 'december_date']
        widgets = {
            'january_date': forms.DateInput(attrs={'class': 'form-control data-list', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'february_date': forms.DateInput(attrs={'class': 'form-control data-list', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'march_date': forms.DateInput(attrs={'class': 'form-control data-list', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'april_date': forms.DateInput(attrs={'class': 'form-control data-list', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'may_date': forms.DateInput(attrs={'class': 'form-control data-list', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'june_date': forms.DateInput(attrs={'class': 'form-control data-list', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'july_date': forms.DateInput(attrs={'class': 'form-control data-list', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'august_date': forms.DateInput(attrs={'class': 'form-control data-list', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'september_date': forms.DateInput(attrs={'class': 'form-control data-list', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'october_date': forms.DateInput(attrs={'class': 'form-control data-list', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'november_date': forms.DateInput(attrs={'class': 'form-control data-list', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'december_date': forms.DateInput(attrs={'class': 'form-control data-list', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
        }