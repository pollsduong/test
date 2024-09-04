from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.say_hello, name='home'),
    path('another_page/', views.another_page, name='another_page'),
]