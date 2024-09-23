# Django Web Authentication

A simple Django application for user authentication, providing features such as registration, login, and password management.

## Features

- User registration and login
- Password reset functionality
- Secure password hashing
- Customizable authentication views

## Technologies Used

- Django
- - HTML/CSS/JavaScript for frontend

## Installation

1. Clone the repository
2. Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
pip install -r requirements.txt

4. Run migrations:
python manage.py migrate

## Usage

Create a superuser (optional):
python manage.py createsuperuser

Start the development server:
python manage.py runserver
