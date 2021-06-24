from django.shortcuts import redirect, render
from .forms import PaymentForm
from .models import Participant, Reviewcenter, Enrolment, Reviewer, Payment


def homepage(request):
	return render(request,'firstpage.html')

def Participants(request):

	user = Participant.objects.create(
		cname = request.POST['cname'],
		add = request.POST['add'],
		num = request.POST['num'],
		school = request.POST['school'],
		)

	return render(request,'reviewcenter.html')

# def Participantts(request):
# 	return render(request,'reviewcenter.html')

def ReviewCenters(request):
	center = Reviewcenter.objects.create(
		reviewcentername = request.POST['reviewcentername'],
		reviewcenteradd = request.POST['reviewcenteradd'],
		)
	return render(request, 'enrollment.html')

def ReviewCenter(request):
	return render(request, 'enrollment.html')


def Enrollmentt(request):
	enroll = Enrolment.objects.create(
		enrollmentdate = request.POST['enrollment'],
		subject = request.POST['sub'],
		session = request.POST['session'],
		schedule = request.POST['sched'],
		)

	return render(request, 'payment.html')

def Enrollment(request):
	return render(request, 'payment.html')

def Paymentt(request):

	bayad = Payment.objects.create(
		place = request.POST['place'],
		test = request.POST['test'],
		quantity = request.POST['quantity'],
		total = request.POST['total'],
		quantity1 = request.POST['quantity1'],
		total1 = request.POST['total1'],
		quantity2 = request.POST['quantity2'],
		total2 = request.POST['total2'],
		)

	return render(request, 'reviewer.html')
	
# def Paymentt(request):
# 	return render(request, 'payment.html')

def Reviewerss(request):

	revs = Reviewer.objects.create(
		# rate = request.POST['rate'],
		strength = request.POST['strength'],
		weakness = request.POST['weakness'],
		suggestion = request.POST['suggestion'],
		comment = request.POST['comment'],
		)

	parti=Participant.objects.last
	pymt=Payment.objects.last

	return render(request, 'summary.html', {'parti':parti,'pymt':pymt,})




def updateResult(request, pk):

	ronan = Payment.objects.get(id=pk)
	form = PaymentForm(instance=ronan)

	if request.method == 'POST':
		form = PaymentForm(request.POST, instance=ronan)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'update.html', context)

def deleteResult(request, pk):
	ronan = Payment.objects.get(id=pk)
	if request.method == "POST":
		ronan.delete()
		return redirect('/')

	context = {'item':ronan}
	return render(request, 'delete.html', context)