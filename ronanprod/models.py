from django.db import models
class User(models.Model):
	pass


class Item(models.Model):

	collab = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)

	#FIRSTNAME
	fname = models.CharField(max_length=50, null=True)
	#MIDDLENAME
	mname = models.CharField(max_length=50, null=True)
	#LASTNAME
	lname = models.CharField(max_length=50, null=True)
	#EXTENSIONNAME
	ename = models.CharField(max_length=50, null=True)
	#EMAIL
	email = models.EmailField(max_length=50, null=True)
	#PASSWORD
	password = models.CharField(max_length=50, null=True)
	#GENDER
	gender = models.CharField(max_length=50, null=True)
	#SUBMIT
	submit1 = models.CharField(max_length=50, null=True)
	

	def __str__(self):
		return self.fname

# Create your models here.
