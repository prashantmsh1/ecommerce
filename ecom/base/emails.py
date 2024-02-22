from django.conf import settings
from django.core.mail import send_mail


def send_account_activation_email(email, email_token):
    subject = "Activate your account"
    email_from = settings.EMAIL_HOST_USER
    message = f"Click the link below to activate your account\n\n   http://127.0.0.1:8000/accounts/activate/{email_token}"
    print("sending email")
    send_mail(subject, message, email_from, [email])
