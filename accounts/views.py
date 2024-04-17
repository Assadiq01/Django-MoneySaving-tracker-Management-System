from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login,  logout, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm, UserEditForm

User = get_user_model()

@login_required
def create_user(user_data):
    user_data['phone_number'] = str(user_data.get('phone_number', ''))

    user = User.objects.create_user(
        email=user_data.get('email', ''),
        username=user_data.get('username', ''),
        password=user_data.get('password', ''),
        first_name=user_data.get('first_name', ''),
        last_name=user_data.get('last_name', ''),
        middle_name=user_data.get('middle_name', ''),
        phone_number=user_data.get('phone_number', ''),
        is_admin=user_data.get("is_admin", '')
    )
    return user

@login_required
def register_user(request):
    user_created = False
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            user_data = registration_form.cleaned_data
            user_data['phone_number'] = str(user_data.get('phone_number', ''))
            
            password = user_data.get('password', '')
            confirm_password = user_data.get('confirm_password', '')

            if password != confirm_password:
                registration_form.add_error('confirm_password', "Passwords do not match.")
                return render(request, 'accounts/register_user.html', {'registration_form': registration_form})
                
            request.session['user_details'] = user_data
            create_user(user_data)
            user_created = True
            
            success_message = "User created successfully!" 
            return render(request, 'accounts/register_user.html', {'success_message': success_message})


        else:
            return render(request, 'accounts/register_user.html', {'registration_form': registration_form})

    else:
        registration_form = UserRegistrationForm()
        success_message = ""

    return render(request, 'accounts/register_user.html', {'registration_form': registration_form, 'success_message': success_message})



def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user_email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            user = authenticate(request, email=user_email, password=password)

            if user is not None:
                login(request, user)

                if user.is_admin or user.is_staff:
                    return redirect('subscribers:subscriber_list')
                else:
                    return redirect('subscribers:subscriber_dashboard', pk=user.subscriber.pk)

            else:
                error_message = "Invalid login credentials. Please try again."
                return render(request, 'accounts/login.html', {'login_form': login_form, 'error_message': error_message})

        else:
            return render(request, 'accounts/login.html', {'login_form': login_form})

    else:
        login_form = LoginForm()

    return render(request, 'accounts/login.html', {'login_form': login_form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('auth:user_login')

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

@login_required
def user_detail(request, user_id):
    user = User.objects.filter(id=user_id).first()
    return render(request, 'accounts/user_detail.html', {'user': user})

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, "Amount updated successfully!")
            return redirect('subscribers:subscriber_detail', pk=user.subscriber.pk)
        else:
            # Form data is invalid, render the form again with errors
            return render(request, 'accounts/edit_user.html', {'edit_form': form, 'user': user})

    else:
        edit_form = UserEditForm(instance=user)
        return render(request, 'accounts/edit_user.html', {'edit_form': edit_form, 'user': user})

@login_required
def delete_user(request, user_id):
    user =  User.objects.filter(id=user_id).first()
    
    if request.method == 'POST':
        user.delete()
        success_message = "User deleted successfully!"
        return redirect('auth:user_list')

    return render(request, 'accounts/delete_user.html', {'user': user})