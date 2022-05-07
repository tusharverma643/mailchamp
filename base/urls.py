from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name="home"),
    # path('send/',views.email, name="send"),
    path('add_email/',views.add_email,name="add_email"),
    path('add_content_type/',views.add_content_type,name="add_content_type"),
    path('add_content/',views.add_content,name="add_content"),
    # path('<str:pk>',views.home, name="home"),
]
