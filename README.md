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

```markdown
5. **Configure SMTP para email functionality:**

   Para habilitar a funcionalidade de redefinição de senha, você precisará configurar as configurações de SMTP. Aqui está como configurá-las usando o Gmail:

   - Vá para as configurações da sua [Conta Google](https://myaccount.google.com/).
   - Navegue até **Segurança**.
   - Sob **Fazendo login no Google**, selecione **Senhas de app**.
   - Você pode precisar habilitar **Verificação em duas etapas** primeiro. Siga os passos para fazer isso.
   - Uma vez habilitada a Verificação em duas etapas, volte para a seção Senhas de app.
   - Selecione **Mail** como o aplicativo e escolha seu dispositivo (ou selecione "Outro" e nomeie algo como "Django App").
   - Clique em **Gerar**. Uma senha de 16 caracteres será exibida.
   - Copie essa senha, pois você precisará dela para suas configurações do Django.

   Em seguida, atualize seu `settings.py` com as seguintes configurações de email:

   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your_email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your_generated_app_password'
```

Make sure to replace 'your_email@gmail.com' with your actual Gmail address and 'your_generated_app_password' with the app password you generated.

## Usage

Create a superuser (optional):
python manage.py createsuperuser

Start the development server:
python manage.py runserver
