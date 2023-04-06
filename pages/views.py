from django.shortcuts import render


# Create your views here.
def home(request):
 return render(request, 'pages/home.html')
def introduction(request):
 return render(request, 'pages/introduction.html')
def map(request):
 return render(request, 'pages/map.html')
def help(request):
 return render(request, 'pages/help.html')

