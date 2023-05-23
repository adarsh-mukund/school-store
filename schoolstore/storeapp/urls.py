
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login.html/', views.login_page, name='login_page'),
    path('register.html/', views.register, name='register'),
    path('formpage.html/', views.form_page, name='form_page'),

]
