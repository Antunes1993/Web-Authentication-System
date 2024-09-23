from .views import *
from django.urls import path

urlpatterns = [
    path('', login_Page, name='login'),
    path('authenticate_user', authenticate_User, name='authenticate_user'),
    path('register', register_New_User, name='register'),
    path('homepage', homepage, name='homepage'),

    path('password_reset/', password_reset_request, name='password_reset'),
    path('reset/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),

]