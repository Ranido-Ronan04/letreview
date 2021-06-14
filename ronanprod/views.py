from django.shortcuts import redirect, render
from .models import Participant, ReviewCenter, Enrollment, Feedback, Schedule


def homepage(request):
	return render(request,'firstpage.html')

def Participants(request):


	# ronan = Participant.objects.create(
	# 	cname = request.POST['cname'],
	# 	add = request.POST['add'],
	# 	num = request.POST['num'],
	# 	school = request.POST['school'],
	# 	)

	return render(request,'reviewcenter.html')

def reviewcenter(request):

	# center = ReviewCenter.objects.create(
	# 	reviewcentername = request.POST['reviewcentername'],
	# 	reviewcenteradd = request.POST['reviewcenteradd'],
	# 	)
	
	return render(request, 'enrollment.html')

# def ReviewCenterr(request):
# 	return render(request, 'enrollment.html')

def enrollment(request):
	# enrol = Enrollment.objects.create(
	# 	enrollmentdate = request.POST['enrollmentdate'],
	# 	subject = request.POST['subject'],
	# 	session = request.POST['session'],
	# 	lecturer = request.POST['lecturer'],
	# 	schedule = request.POST['schedule'],
	# 	payment = request.POST['payment'],
	# 	)
	return render(request, 'enrollment.html')

def Feed(request):
	return render(request, 'feedback.html')

def Enroll(request):
	return render(request, 'enrollment.html')

def Review(request):
	return render(request, 'reviewer.html')

