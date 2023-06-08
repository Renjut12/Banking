from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [

    path('Home/',views.Home,name='Home'),
    path('Login/',views.Login,name='Login'),
    path('Register/',views.Register,name='Register'),
    path('new/',views.new,name='new'),
    path('form/',views.form,name='form'),
    path('Ernakulam/',views.Ernakulam,name='Ernakulam'),
    path('Kollam/',views.Kollam,name='Kollam'),
    path('Pathanamthitta/',views.Pathanamthitta,name='Pathanamthitta'),
    path('Kottayam/',views.Kottayam,name='Kottayam'),
    path('Thiruvananthapuram/',views.Thiruvananthapuram,name='Thiruvananthapuram'),

]
