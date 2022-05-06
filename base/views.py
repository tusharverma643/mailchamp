from multiprocessing import context
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from .forms import ContentForm, ContentTypeForm, EmailForm
from .models import Content
from django.utils.timezone import localtime 
# Create your views here.


def home(request):
    emailform = EmailForm()
    content_type_form = ContentTypeForm()
    content_form= ContentForm()
    context= {'form': emailform,'content_type_form': content_type_form,'content_form': content_form}
    return render(request,'base/home.html',context)  
 

def add_email(request):
    if request.method == 'POST':
        form=EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

def add_content_type(request):
    if request.method == 'POST':
        form=ContentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

def add_content(request):
    if request.method == 'POST':
        form=ContentForm(request.POST)
        if form.is_valid():
            content=Content()
            content.content_type=form.cleaned_data['content_type']
            content.subject=form.cleaned_data['subject']
            content.content_text=form.cleaned_data['content_text']
            content.sending_datetime=localtime(form.cleaned_data['sending_datetime'])
            content.save()
            return redirect('home')

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['tverma_be19@thapar.edu',]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'base/home.html')

 