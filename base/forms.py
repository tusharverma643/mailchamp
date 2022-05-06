from django import forms
from django import forms
from django.forms import ModelForm
from .models import Email,ContentType,Content

class EmailForm(ModelForm):
    class Meta:
        model=Email
        fields= '__all__'

class ContentTypeForm(ModelForm):
    class Meta:
        model=ContentType
        fields= '__all__'

class DateTimeInput(forms.DateTimeInput):
    input_type='datetime-local'
        
class ContentForm(ModelForm):
    sending_datetime=forms.DateTimeField(widget=DateTimeInput)
    class Meta:
        model=Content
        fields= ['content_type','subject','content_text']
    