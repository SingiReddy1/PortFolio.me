from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from projectResume.models import AddMsg
from django.contrib import messages


# Create your views here.

def home(request):
    n = ''
    if request.method == 'POST':
        name = request.POST['name']
        msg = request.POST['msg']
        email = request.POST['email']

        new_msg = AddMsg(name=name, msg=msg, email=email)
        new_msg.save()
    return render(request, 'index.html')
