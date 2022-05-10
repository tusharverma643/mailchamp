from django.db import models

# Create your models here.

#Model storing Emails of all recipients.
class Email(models.Model):
    email = models.EmailField(max_length=254,primary_key=True)

    def __str__(self):
        return str(self.email)

#Model storing Content type and Email Info of all recipients. Note there is a Many to Many relationship between Content-Type(Topic) and Email
class ContentType(models.Model):
    content_type=models.CharField(max_length=100,primary_key=True)
    emails = models.ManyToManyField(Email)

    def __str__(self):
        return self.content_type[0:40]
#Model to store the content to be sent. Note there is One to Many relationship between Content type(Topic) and Content. Thus using Foreign key.
class Content(models.Model):
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE,blank=True)
    subject=models.CharField(max_length=250,blank=True,null=True)
    content_text=models.TextField(blank=True,null=True)
    sending_datetime=models.DateTimeField(null=True,blank=True)

    class Meta:
        ordering = ['sending_datetime'] #storing mails to be sent in ascending order.
    def __str__(self):
        return self.content_text[0:100]

    