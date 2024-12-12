from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

# View for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# View for managing users, restricted to superusers
@login_required
@user_passes_test(lambda user: user.is_superuser)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'manage_users.html', {'users': users})

# View restricted to logged-in users
@login_required
def restricted_view(request):
    return render(request, 'restricted.html')

# Function to check if the user is an admin (superuser)
def is_admin(user):
    return user.is_superuser

# View restricted to admin (superuser) users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_only.html')