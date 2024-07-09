from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def gallery(request):
    return render(request,'gallery.html')

def info(request):
    return render(request,'info.html')

def form(request):
    return render(request,'form.html')

def login(request):
    return render(request, 'log in.html')

def registration(request):
    return render(request,'registration.html')