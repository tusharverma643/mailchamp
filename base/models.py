from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Email(models.Model):
    email = models.EmailField(max_length=254,primary_key=True)

    def __str__(self):
        return str(self.email)


class ContentType(models.Model):
    content_type=models.CharField(max_length=100,primary_key=True)
    emails = models.ManyToManyField(Email)

    def __str__(self):
        return self.content_type[0:40]

class Content(models.Model):
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    subject=models.CharField(max_length=250,blank=True)
    content_text=models.TextField()
    sending_datetime=models.DateTimeField()
#there can be multiple topics ie content_type with different con
    def __str__(self):
        return self.content_text[0:100]

    