from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from appcom.models import Customerdb
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *

# Create your views here.
def index(request):
	return render(request, 'index.html')
	#return HttpResponse("<h1>This is home Page<h1>")
def about(request):
	
	return render(request, 'about.html')



def Register(request):
	form = UserCreationForm()
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form': form}
	return render(request, 'Register.html', context)
def contact(request):
	if request.method=='POST':
		cuname = request.POST.get('cuname')
		cumail = request.POST.get('cumail')
		Discription = request.POST.get('Discription')
		contact = Customerdb(cuname=cuname, cumail=cumail, Discription=Discription, pubdate=datetime.today())
		contact.save()
		messages.success(request, 'message has been sent.')
	return render(request, 'contact.html')
