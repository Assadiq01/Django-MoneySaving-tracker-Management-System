# subscribers/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SubscriberForm, DaySavingForm
from .models import Subscriber, DaySaving
from accounts.models import User
from itertools import groupby
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, SubscriberForm
import calendar
from django.db.models import Q
from django.http import HttpResponse

@login_required
def subscriber_register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        subscriber_form = SubscriberForm(request.POST)

        if user_form.is_valid() and subscriber_form.is_valid():
            user = user_form.save()
            subscriber_form.save(user=user)
            login(request, user)
            return redirect('subscribers:subscriber_list')
    else:
        user_form = CustomUserCreationForm()
        subscriber_form = SubscriberForm()

    return render(request, 'subscribers/subscriber_register.html', {'user_form': user_form, 'subscriber_form': subscriber_form})

@login_required
def subscriber_list(request):
    all_subscribers = Subscriber.objects.all()
    all_users = User.objects.all()
    query = request.GET.get('q')

    if query:
        users = all_users.filter(Q(first_name__icontains=query))

    context = {
        'all_subscribers': all_subscribers
    }
    return render(request, 'subscribers/subscriber_list.html', context)

@login_required
def subscriber_detail(request, pk):
    subscriber = get_object_or_404(Subscriber, pk=pk)
    day_savings = DaySaving.objects.filter(subscriber=subscriber)

    grouped_by_month = {}

    # Iterate over each month
    for month in range(1, 13):
        month_data = []
        for day_saving in day_savings:
            # Get the date for the current month
            date_for_month = getattr(day_saving, f"{calendar.month_name[month].lower()}_date")
            if date_for_month and date_for_month.month == month:  # Check if the date is for the current month
                month_data.append(day_saving)
        grouped_by_month[calendar.month_name[month]] = month_data



    # Prepare the context
    context = {
        'subscriber': subscriber,
        'grouped_by_month': grouped_by_month,
        'day_savings' : day_savings,
    }
    
    return render(request, 'subscribers/subscriber_detail.html', context)


@login_required
def subscriber_dashboard(request, pk):
    subscriber = get_object_or_404(Subscriber, pk=pk)
    day_savings = DaySaving.objects.filter(subscriber=subscriber)

    grouped_by_month = {}

    # Iterate over each month
    for month in range(1, 13):
        month_data = []
        for day_saving in day_savings:
            # Get the date for the current month
            date_for_month = getattr(day_saving, f"{calendar.month_name[month].lower()}_date")
            if date_for_month and date_for_month.month == month:  # Check if the date is for the current month
                month_data.append(day_saving)
        grouped_by_month[calendar.month_name[month]] = month_data



    # Prepare the context
    context = {
        'subscriber': subscriber,
        'grouped_by_month': grouped_by_month,
        'day_savings' : day_savings,
    }
    
    return render(request, 'subscribers/subscriber_dashboard.html', context)

@login_required
def subscriber_add(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscribers:subscriber_list')
    else:
        form = SubscriberForm()

    return render(request, 'subscribers/subscriber_add.html', {'form': form})

@login_required
def subscriber_edit(request, pk):
    subscriber = get_object_or_404(Subscriber, pk=pk)

    if request.method == 'POST':
        form = SubscriberForm(request.POST, instance=subscriber)
        if form.is_valid():
            form.save()
            return redirect('subscribers:subscriber_list')
    else:
        form = SubscriberForm(instance=subscriber)

    return render(request, 'subscribers/subscriber_edit.html', {'form': form})

@login_required
def subscriber_delete(request, pk):
    subscriber = get_object_or_404(Subscriber, pk=pk)
    
    if request.method == 'POST':
        subscriber.delete()
        return redirect('subscribers:subscriber_list')

    return render(request, 'subscribers/subscriber_delete.html', {'subscriber': subscriber})

@login_required
def saving(request, subscriber_id):
    subscriber = get_object_or_404(Subscriber, pk=subscriber_id)

    if request.method == 'POST':
        form = DaySavingForm(request.POST)
        if form.is_valid():
            new_day_saving = form.save(commit=False)
            new_day_saving.subscriber = subscriber
            new_day_saving.save()
            return redirect('subscribers:subscriber_detail', pk=subscriber_id)
    else:
        form = DaySavingForm()

    return render(request, 'subscribers/saving.html', {'subscriber': subscriber, 'form': form})

@login_required
def day_saving_form(request, subscriber_id, day_saving_id):
    subscriber = get_object_or_404(Subscriber, pk=subscriber_id)
    day_saving = get_object_or_404(DaySaving, pk=day_saving_id)

    if request.method == 'POST':
        form = DaySavingForm(request.POST, instance=day_saving)
        if form.is_valid():
            form.save()
            return redirect('subscribers:subscriber_detail', pk=subscriber_id)
    else:
        form = DaySavingForm(instance=day_saving)

    return render(request, 'subscribers/day_saving_form.html', {'subscriber': subscriber, 'form': form, 'day_saving': day_saving})

def delete_month_dates(request, subscriber_id, month):
    subscriber = get_object_or_404(Subscriber, pk=subscriber_id)
    day_savings_to_delete = DaySaving.objects.filter(subscriber=subscriber)

    # Filter day savings for the specified month and delete them
    for day_saving in day_savings_to_delete:
        date_for_month = getattr(day_saving, f"{calendar.month_name[month].lower()}_date")
        if date_for_month and date_for_month.month == month:
            day_saving.delete()

    return redirect('subscribers:subscriber_detail', pk=subscriber_id)