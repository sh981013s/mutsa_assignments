from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def aboutme(request):
    return render(request, 'aboutme.html')

def whatdoilike(request):
    return render(request, 'whatdoilike.html')
# Create your views here.
