from django.shortcuts import render, HttpResponse
from .models import Item


# Create your views here.
def Mainpage(request):
	
	
	if request.method == 'POST':
		
		fname = request.POST['fname']
		mname = request.POST['mname']
		lname = request.POST['lname']
		ename = request.POST['ename']
		email = request.POST['emails']
		password = request.POST['password1']
		gender = request.POST['gender']
		submit = request.POST['submit1']

		
		yey = Item()
		yey.fname = fname
		yey.mname = mname
		yey.lname = lname
		yey.ename = ename
		yey.email = email
		yey.password = password
		yey.gender = gender
		yey.submit = submit
		yey.save()



	return render(request,'Mainpage.html')	


def Page(request):
	yey = Item.objects.all().order_by('fname')
	return render(request,'mainpage1.html', {'yey':yey})

# Create your views here.


# Create your views here.
