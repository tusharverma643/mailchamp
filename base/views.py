from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ContentForm, ContentTypeForm, EmailForm
from .models import Content
from django.utils.timezone import localtime 
# Create your views here.

#render Forms on the home page.
def home(request):
    emailform = EmailForm()
    content_type_form = ContentTypeForm()
    content_form= ContentForm()
    context= {'email_form': emailform,'content_type_form': content_type_form,'content_form': content_form}
    return render(request,'base/home.html',context)  
 
#view to add email
def add_email(request):
    if request.method == 'POST':
        form=EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

#view to add content type
def add_content_type(request):
    if request.method == 'POST':
        form=ContentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

#view to add content ie Email to be sent.
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


 