from django.db import models



class Let(models.Model):

	#Taker's Name
	name = models.CharField(max_length=50, null=True)
	#Taker's address
	address = models.CharField(max_length=50, null=True)
	#Taker's Contact
	contact = models.CharField(max_length=50, null=True)
	#Taker's Type
	# tchoice = (('teacher','Teacher'),('graduate','Graduate'))
	# appli = models.TextField(choices=tchoice, default='none')
	#School
	school = models.CharField(max_length=50, null=True)
	#Taker's course
	course = models.CharField(max_length=50, null=True)
	#Birthday
	Birthday = models.DateField(max_length=50, null=True)
	#gender
	Gender =(('gender', 'Male'), ('gender', 'Female'))
	Gender =models.CharField(max_length=10, choices=Gender, default='none')
	#Taker's choice
	# rchoice = (('sr','Self Review'),('rc','Review Center'))
	# style = models.TextField(choices=rchoice, default='none')

	def __str__(self):
		return self.name



class Center(models.Model):

	user = models.ForeignKey(Let, default=None, on_delete=models.CASCADE, null=True)

	#Center's Name
	Name_of_the_Review_Center = models.CharField(max_length=50, null=True)
	#Center's address
	Address_of_the_Review_Center = models.CharField(max_length=50, null=True)
	#Lecturer's Name
	Name_of_the_Lecturer = models.CharField(max_length=50, null=True)
	#Center's fee
	Payment = models.IntegerField(null=True)
	#Schedule
	Schedule_of_the_Review = models.DateField(max_length=50, null=True)
	
	

	def __str__(self):
		return self.Name_of_the_Review_Center





class Exam(models.Model):

	user = models.ForeignKey(Let, default=None, on_delete=models.CASCADE, null=True)

	#Name of the School
	Name_of_the_School = models.CharField(max_length=50, null=True)
	#Address of the school
	Address_of_the_School = models.CharField(max_length=50, null=True)
	#Date of review
	Date_of_the_Exam = models.DateTimeField(null=True)
	#Subject
	# schoice = (('gened','General Education'),('profed','Profession Educaction'),('ict','Information and Communication Technology'))
	# subject = models.TextField(choices=schoice, default='none')
	#Summary of review
	# summary = models.CharField(max_length=50, null=True)
	
	

	def __str__(self):
		return self.Name_of_the_School






# class Selfreview(models.Model):

# 	user = models.ForeignKey(Let, default=None, on_delete=models.CASCADE, null=True)

# 	#Date of review
# 	date = models.DateTimeField(null=True)
# 	#Subject
# 	schoice = (('gened','General Education'),('profed','Profession Educaction'),('ict','Information and Communication Technology'))
# 	subject = models.TextField(choices=schoice, default='none')
# 	#Summary of review
# 	summary = models.CharField(max_length=50, null=True)
	
	

# 	def __str__(self):
# 		return self.summary





class Feedback(models.Model):

	user = models.ManyToManyField(Let)

	#Date of exam
	# exam = models.DateTimeField(null=True)
	#Result of the exam
	# stchoice = (('passed','Passed'),('failed','Failed'))
	# status = models.TextField(choices=stchoice, default='none')
	#strength
	strength = models.CharField(max_length=50, null=True)
	#weakness
	weakness = models.CharField(max_length=50, null=True)
	#comments
	comment = models.CharField(max_length=50, null=True)
	#Ssuggestion
	suggestion = models.CharField(max_length=50, null=True)	
	
	

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
