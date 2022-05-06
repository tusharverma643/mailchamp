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
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE,blank=True)
    subject=models.CharField(max_length=250,blank=True,null=True)
    content_text=models.TextField(blank=True,null=True)
    sending_datetime=models.DateTimeField(null=True,blank=True)
#there can be multiple topics ie content_type with different con

    class Meta:
        ordering = ['sending_datetime']
    def __str__(self):
        return self.content_text[0:100]

    