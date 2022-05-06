from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
# Create your views here.


def home(request):
    # context={'num': pk}
    return render(request,'base/home.html')

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['tverma_be19@thapar.edu',]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'base/home.html')

