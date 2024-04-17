from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User


class UserAdmin(admin.ModelAdmin):
    ordering = ('email',) 
    list_display = ('email', 'first_name', 'last_name', 'is_active',
              'last_login', 'date_joined')
    list_filter = ('is_active',)

admin.site.register(User, UserAdmin)