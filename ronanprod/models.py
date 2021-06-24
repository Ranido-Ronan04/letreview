from django.db import models



class Participant(models.Model):

	cname = models.CharField(max_length=50, null=True)
	add = models.CharField(max_length=50, null=True)
	school = models.CharField(max_length=50, null=True)
	num = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.cname


class Reviewcenter(models.Model):

	user = models.ForeignKey(Participant, default=None, on_delete=models.CASCADE, null=True)

	reviewcentername = models.CharField(max_length=50, null=True)
	reviewcenteradd = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.reviewcentername


class Enrolment(models.Model):

	user = models.ForeignKey(Participant, default=None, on_delete=models.CASCADE, null=True)

	enrollmentdate = models.DateTimeField(null=True)
	sub = (
		('profed','Professional Education'),
		('gened','General Education'),
		('tle','Technology and Livelihood Education'),
		)
	subject = models.CharField(max_length=50, choices=sub, default='sub1')
	session = models.IntegerField(null=True)
	# lecturer = models.CharField(max_length=50, null=True)
	sched = (
		('monday','Monday'),
		('tuesday','Tuesday'),
		('wednesday','Wednesday'),
		('thursday','Thursday'),
		('friday','Friday'),
		('saturday','Saturday'),
		('sunday','Sunday'),
		)
	schedule = models.CharField(max_length=50, choices=sched, default='monday')
	# payment = models.CharField(max_length=50, null=True)


class Reviewer(models.Model):

	user = models.ManyToManyField(Participant)

	# rate = models.IntegerField(max_length=50, default=0)
	comment = models.CharField(max_length=1000, null=True)
	strength = models.CharField(max_length=1000, null=True)
	weakness = models.CharField(max_length=1000, null=True)
	suggestion = models.CharField(max_length=1000, null=True)	

	def __str__(self):
		return self.comment


class Payment(models.Model):

	user = models.ManyToManyField(Participant)

	place = models.CharField(max_length=1000, null=True)
	test = models.DateField(max_length=50, null=True)
	quantity = models.CharField(max_length=100, null=True)
	total = models.CharField(max_length=50, null=True)
	quantity1 = models.CharField(max_length=50, null=True)
	total1 = models.CharField(max_length=50, null=True)
	quantity2 = models.CharField(max_length=50, null=True)
	total2 = models.CharField(max_length=50, null=True)
	# disc = models.CharField(max_length=50, null=True)
	# totalCost = models.IntegerField( null=True)


	def __str__(self):
		return self.place

