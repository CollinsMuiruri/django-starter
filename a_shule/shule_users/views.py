from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def custom_login(request):
    # Redirect to homepage if the user is already logged in
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('home')  # Replace 'home' with the name of your homepage URL
    
    if request.method == 'POST':
        username = request.POST.get('username')  # This can be either email or phone number
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # Use username for authentication

        if user is not None:
            login(request, user)
            return render(request, 'shule_users/login_success.html')  # Redirect to dashboard or another page
        else:
            return render(request, 'shule_users/login_error.html', {'error': 'Invalid email, phone number, or password.'})

    return render(request, 'shule_users/login.html')

    

def custom_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')    