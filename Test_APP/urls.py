from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('centerPage/', views.center, name='center'),
    path('header', views.header, name='header'),
    path('email/', views.email, name='email'),
    path('contact/', views.contact, name='contact'),
]

urlpatterns += staticfiles_urlpatterns()
