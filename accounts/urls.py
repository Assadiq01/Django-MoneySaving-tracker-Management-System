# subscribers/urls.py
from django.urls import path
from .views import register_user, user_login, user_list, user_detail, \
    user_detail, edit_user, delete_user, user_logout

app_name = 'auth'

urlpatterns = [
    path('register/', register_user, name='user_registration'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('users/', user_list, name='user_list'),
    path('users/<int:user_id>/', user_detail, name='user_detail'),
    path('edit/<int:user_id>/', edit_user, name='edit_user'),
    path('delete/<int:user_id>/', delete_user, name='delete_user')
]
