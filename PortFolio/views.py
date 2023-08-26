from django.shortcuts import render
from projectResume.models import AddMsg

def home(request):
    return render(request, 'index.html')


