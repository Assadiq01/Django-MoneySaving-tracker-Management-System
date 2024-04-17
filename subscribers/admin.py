# subscribers/admin.py
from django.contrib import admin
from .models import Subscriber, DaySaving
from .forms import DaySavingForm


admin.site.register(Subscriber)
admin.site.register(DaySaving)
