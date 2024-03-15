from django.core.mail import send_mail
import uuid
from CarDealerProject import settings

def send_forgot_pass(Email,token):

    subject = "Your forgot password link"
    message = f'click on the link to reset your password...http://127.0.0.1:8000/Frontend/change_password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient= [Email]
    send_mail(subject,message,email_from,recipient)
    return True
