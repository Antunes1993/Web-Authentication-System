from django.shortcuts import redirect
from django.shortcuts import render
from .forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

def login_Page(request):
    return render(request, 'login_page.html')

def homepage(request):
    return render(request, 'homepage.html')

def authenticate_User(request):
    user = None
    username = request.POST['username'].lower()
    password = request.POST['password']

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
            return redirect(Login_Page)

        # Authenticate user
        user = authenticate(request, username=username, password=password)

    #Check if authentication is ok
    if user is not None:
        login(request, user)
        return redirect('homepage')
    else:
        messages.error(request, "Incorrect login or password.")
    return redirect('login')

def register_New_User(request):
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
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                messages.success(request, "Congrats! Your user was created!")
                return redirect('login')
    else:
        form = RegisterUserForm()

    return render(request, 'register_user.html', {'form': form})

def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            password_reset_url = f'http://127.0.0.1:8001/reset/{uid}/{token}/'

            send_mail(
                'Password Reset Request',
                f'Please click the link to reset your password: {password_reset_url}',
                'djangoapp15@gmail.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, "Password reset link sent!")
            return redirect('login')
        else:
            messages.error(request, "Email not found.")
    return render(request, 'password_reset_form.html')

def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)

        if default_token_generator.check_token(user, token):
            if request.method == 'POST':
                new_password = request.POST.get('password')
                user.set_password(new_password)
                user.save()
                messages.success(request, "Password has been reset successfully.")
                return redirect('login')
            return render(request, 'password_reset_confirm.html', {'valid_token': True})
        else:
            messages.error(request, "Invalid token.")
            return redirect('password_reset_request')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, "Invalid request.")
        return redirect('password_reset_request')