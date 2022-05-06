from django.contrib import admin
from .models import Content,ContentType,Email
# Register your models here.

admin.site.register(Email)
admin.site.register(ContentType)
admin.site.register(Content)
