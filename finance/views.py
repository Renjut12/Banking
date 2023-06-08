from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'Home.html')

def Login(request):
    return render(request,'Login.html')

def Register(request):
    return render(request,'Register.html')

def new(request):
    return render(request,'Newpage.html')

def form(request):
    return render(request,'Registrationform.html')

def Ernakulam(request):
    return render(request,'Ernakulam.html')

def Kollam(request):
    return render(request,'Kollam.html')

def Pathanamthitta(request):
    return render(request,'Pathanamthitta.html')

def Kottayam(request):
    return render(request,'Kottayam.html')

def Thiruvananthapuram(request):
    return render(request,'Thiruvananthapuram.html')

