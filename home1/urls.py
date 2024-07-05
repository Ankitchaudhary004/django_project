from django.contrib import admin
from django.urls import path
from home1 import views

urlpatterns = [
    path("",views.showView,name='home'),
    path("about",views.showAbout,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path('login/', views.login_view, name='login'),
    path('yyyt/', views.yt, name='yt'),

]