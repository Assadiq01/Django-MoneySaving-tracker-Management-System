from django.urls import path
from .views import subscriber_register, subscriber_dashboard, \
    saving, day_saving_form, subscriber_list, subscriber_detail, \
    subscriber_add, subscriber_edit, subscriber_delete, delete_month_dates

app_name = 'subscribers'

urlpatterns = [
    path('subscriber-list/', subscriber_list, name='subscriber_list'),
    path('subscriber-register/', subscriber_register, name='subscriber_register'),
    path('subscriber/<int:pk>/', subscriber_detail, name='subscriber_detail'),
    path('subscriber/<int:pk>/dashboard/', subscriber_dashboard, name='subscriber_dashboard'),  # Changed URL pattern for subscriber_dashboard
    path('subscriber/add/', subscriber_add, name='subscriber_add'),
    path('subscriber/<int:pk>/edit/', subscriber_edit, name='subscriber_edit'),
    path('subscriber/<int:pk>/delete/', subscriber_delete, name='subscriber_delete'),

    path('subscriber/<int:subscriber_id>/choice/', saving, name='saving'),
    path('subscriber/<int:subscriber_id>/choice/day_saving_form/<int:day_saving_id>/', day_saving_form, name='day_saving_form'),
    path('subscribers/subscriber/<int:subscriber_id>/delete_month_dates/<int:month>/', delete_month_dates, name='delete_month_dates'),
]
