from django.shortcuts import redirect, render
from .models import Item, User

# Create your views here.
def Mainpage(request):
	
	if request.method == 'POST':

		collab = User.objects.create()
		Item.objects.create(
			fname = request.POST['fname'],
			mname= request.POST['mname'], 
			lname = request.POST['lname'],
			ename = request.POST['ename'], 
			email = request.POST['emails'],
			password = request.POST['password1'],
			gender = request.POST['gender'],
			submit1 = request.POST['submit1'],
			)
		return redirect('oks')
# from django.shortcuts import redirect, render
# from .models import Item, User


# # Create your views here.
# def Mainpage(request):
	
# 	if request.method == 'POST':

# 		collab = User.objects.create()
# 		Item.objects.create(
# 			fname = request.POST['fname'],
# 			mname = request.POST['mname'], 
# 			lname = request.POST['lname'],
# 			ename = request.POST['ename'], 
# 			email = request.POST['email'],
# 			password = request.POST['password'],
# 			gender = request.POST['gender'],
# 			submit = request.POST['submit'],
# 			)
# 		return redirect('oks')
	# if request.method == 'POST':
		
	# 	fname = request.POST['fname']
	# 	mname = request.POST['mname']
	# 	lname = request.POST['lname']
	# 	ename = request.POST['ename']
	# 	email = request.POST['emails']
	# 	password = request.POST['password1']
	# 	gender = request.POST['gender']
	# 	submit = request.POST['submit1']

		
		yey = Item()
		yey.fname = fname
		yey.mname = mname
		yey.lname = lname
		yey.ename = ename
		yey.emails = emails
		yey.password1 = password1
		yey.gender = gender
		yey.submit1 = submit1
		yey.save()

	return render(request,'Mainpage.html')

def Page(request):
	yey = Item.objects.all().order_by('fname')
	return render(request,'mainpage1.html', {'yey':yey})

# Create your views here.


# Create your views here.
