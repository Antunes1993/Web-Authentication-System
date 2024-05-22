from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from .forms import RegisterUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def Login_Page(request):
    return render(request, 'login_page.html')

def Authenticate_User(request):
    print("2233334433")
    user = None
    username = request.POST['username'].lower()
    password = request.POST['password']
    print(username, password)
    #Check if username or password fields are left in blank.
    if not(username and password):
        messages.error(request, "The username and password fields cannot be left in blank.")
        return redirect(Login_Page)

    #Check if user exists in database
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)

        # Check if user is activated in database.
        if (not user.is_active) or (user.groups.filter(name="Non_Approved_Users").exists()):
            messages.error(request, "Your profile is not activated. Please contact the administrator.")
            return redirect('login_page')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

    #Check if authentication is ok
    if user is not None:
        login(request, user)
        return redirect('homepage')
    else:
        messages.error(request, "Incorrect login or password.")

    return redirect('login_page')


def Register_New_User(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Already is registered user with this email.")
            else:
                form.save()
                messages.success(request, "Registration Successful.")
                return redirect('login_page')
    else:
        form = RegisterUserForm()

    return render(request, 'register_user.html', {'form': form})

def Homepage(request):
    return render(request, 'homepage.html')