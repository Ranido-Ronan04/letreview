from django.db import models



class Participant(models.Model):

	cname = models.CharField(max_length=50, null=True)
	add = models.CharField(max_length=50, null=True)
	school = models.CharField(max_length=50, null=True)
	num = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.cname


class ReviewCenter(models.Model):

	user = models.ForeignKey(Participant, default=None, on_delete=models.CASCADE, null=True)

	#Center's Name
	reviewcentername = models.CharField(max_length=50, null=True)
	#Center's address
	reviewcenteradd = models.CharField(max_length=50, null=True)
	# #Lecturer's Name
	# Name_of_the_Lecturer = models.CharField(max_length=50, null=True)
	# #Center's fee
	# Payment = models.IntegerField(null=True)
	# #Schedule
	# Schedule_of_the_Review = models.DateField(max_length=50, null=True)
	
	

	def __str__(self):
		return self.reviewcentername

class Enrollment(models.Model):

	user = models.ForeignKey(Participant, default=None, on_delete=models.CASCADE, null=True)

	enrollmentdate = models.DateTimeField(null=True)
	sub = (
		('profed','Professional Education'),
		('gened','General Education'),
		('tle','Technology and Livelihood Education'),
		)
	subject = models.CharField(max_length=50, choices=sub, default='sub1')
	session = models.IntegerField(null=True)
	lecturer = models.CharField(max_length=50, null=True)
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
	payment = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.enrollmentdate


class Schedule(models.Model):

	user = models.ForeignKey(Participant, default='', on_delete=models.CASCADE, null=True)

	place = models.CharField(max_length=50, null=True)
	examdate = models.DateTimeField(null=True)

	def __str__(self):
		return self.place

# class Exam(models.Model):

# 	user = models.ForeignKey(Participant, default=None, on_delete=models.CASCADE, null=True)

# 	#Name of the School
# 	Name_of_the_School = models.CharField(max_length=50, null=True)
# 	#Address of the school
# 	Address_of_the_School = models.CharField(max_length=50, null=True)
# 	#Date of review
# 	Date_of_the_Exam = models.DateTimeField(null=True)
	

# 	def __str__(self):
# 		return self.Name_of_the_School


class Feedback(models.Model):

	user = models.ManyToManyField(Participant)

	#Date of exam
	# exam = models.DateTimeField(null=True)
	#Result of the exam
	# stchoice = (('passed','Passed'),('failed','Failed'))
	# status = models.TextField(choices=stchoice, default='none')
	#strength
	strength = models.CharField(max_length=1000, null=True)
	#weakness
	weakness = models.CharField(max_length=1000, null=True)
	#comments
	comment = models.CharField(max_length=1000, null=True)
	#Ssuggestion
	suggestion = models.CharField(max_length=1000, null=True)	
	
	

	def __str__(self):
		return self.strength







# class Feedback(models.Model):

# 	user = models.ManyToManyField(Tupc)

# 	#strength
# 	strength = models.CharField(max_length=50, null=True)
# 	#weakness
# 	weakness = models.CharField(max_length=50, null=True)
# 	#Ssuggestion
# 	suggestion = models.CharField(max_length=50, null=True)
	
	
	

# 	def __str__(self):
# 		return self.strength
