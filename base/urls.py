from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name="home"),
    path('send/',views.email, name="email"),
    # path('<str:pk>',views.home, name="home"),

]
