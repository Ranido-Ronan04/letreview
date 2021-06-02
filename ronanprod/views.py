from django.shortcuts import redirect, render
from .models import Let, Center, Exam, Feedback

# def html1(request):

# 	return render(request,'html1.html')

# def Let(request):

# 	user=Let.objects.create(
# 		cname = request.POST['cname'],
# 		add = request.POST['add'],
# 		num = request.POST['num'],
# 		school = request.POST['school'],
# 		course = request.POST['course'],
# 		# profession = request.POST[('teacher','Teacher'),('grad','Graduate')],
# 		bday = request.POST['bday'],
# 		gender = request.POST['gender']
# 		# review = request.POST[('sr','Self Review'),('rc','Review Center')],
# 		)

# 	return render(request,'reviewcenter.html')
# 	return redirect('nan')

def html1(request):

	if request.method == 'POST':

		name = Let.objects.create(
			cname = request.POST['cname'],
			add = request.POST['add'],
			num = request.POST['num'],
			school = request.POST['school'],
			course = request.POST['course'],
			bday = request.POST['bday'],
			gender = request.POST['gender'],
			submit = request.POST['submit']
			# gradelevel = request.POST['gradelevel'],
			# name = request.POST['name'], 
			# lrn = request.POST['lrn'],
			# birthday = request.POST['birthday'], 
			# address = request.POST['address'],
			)

		return redirect('Center')
		
		nan = Let()
		nan.cname = cname
		nan.add = add
		nan.num = num
		nan.school = school
		nan.course = course
		nan.bday = bday
		nan.gender = gender
		nan.submit = submit
		nan.save()

	return render(request,'firstpage.html')
	# return redirect('nan')

def Center(request):
	
	nan = Center.objects.all().order_by('name')
	return redirect(request,'reviewcenter.html', {'nan': nan})

# def
#  Omepage(request):

# 	if request.method == 'POST':

# 		enroll = Student.objects.create()
# 		Student.objects.create(
# 			gradelevel = request.POST['gradelevel'],
# 			name = request.POST['name'], 
# 			lrn = request.POST['lrn'],
# 			birthday = request.POST['birthday'], 
# 			address = request.POST['address'],
# 			)

# 		return redirect('students')
		
# 		abg = Student()
# 		abg.gradelevel = gradelevel
# 		abg.name = name
# 		abg.lrn = lrn
# 		abg.birthday = birthday
# 		abg.address = address
# 		abg.save()

# 	return render(request,'Omepage.html')

# def
#  Page(request):
	
# 	abg = Student.objects.all().order_by('gradelevel')
# 	return render(request,'students.html', {'abg': abg})


# def Reviewc(request):

# 	# customerId=Customer.objects.get(id=customerId)

# 	resortId=Resort.objects.create(
# 		resort = request.POST['resort'])

# 	admitId=Admission.objects.create(
# 		entrance = request.POST['entrance'],
# 		admit = request.POST['admit'],
# 		)

# 	cottageId=Cottage.objects.create(
# 		cottage = request.POST['cottage'])

# 	return render(request,'receipt.html')
