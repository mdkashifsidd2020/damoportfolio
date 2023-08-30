from django.shortcuts import render
from .models import *
import tinme

# Create your views here.
def index(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        mydata=dform(name='name',email='email',subject='subject',message='message')
        mydata.save()
    return render(request , "index.html")
