# Django Web Authentication

A simple Django application for user authentication, providing features such as registration, login, and password management.

## Features

- User registration and login
- Password reset functionality
- Secure password hashing
- Customizable authentication views

## Technologies Used

- Django
- HTML/CSS/JavaScript for frontend

## Installation

1. Clone the repository
2. Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
pip install -r requirements.txt

4. Run migrations:
python manage.py migrate

5. Configure SMTP for email functionality:

To enable password reset functionality, you'll need to configure SMTP settings. Here’s how to set it up using Gmail:

Go to your Google Account settings.
Navigate to Security.
Under Signing in to Google, select App passwords.
You may need to enable 2-Step Verification first. Follow the prompts to do so.
Once 2-Step Verification is enabled, return to the App passwords section.
Select Mail as the app and choose your device (or select "Other" and name it something like "Django App").
Click Generate. A 16-character password will be displayed.
Copy this password, as you will need it for your Django settings.
Next, update your settings.py with the following email configuration:

python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_generated_app_password'


Make sure to replace 'your_email@gmail.com' with your actual Gmail address and 'your_generated_app_password' with the app password you generated.

## Usage

Create a superuser (optional):
python manage.py createsuperuser

Start the development server:
python manage.py runserver
