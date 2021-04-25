from django.db import models

class Item(models.Model):
	#FIRSTNAME
	fname = models.CharField(max_length=50, null=True)
	#MIDDLENAME
	mname = models.CharField(max_length=50, null=True)
	#LASTNAME
	lname = models.CharField(max_length=50, null=True)
	#EXTENSIONNAME
	ename = models.CharField(max_length=50, null=True)
	#EMAIL
	email = models.CharField(max_length=50, null=True)
	#PASSWORD
	password = models.CharField(max_length=50, null=True)
	#GENDER
	gender = models.CharField(max_length=50, null=True)
	#email = models.CharField(max_length=50, null=True)
	#BODY
	#body = models.TextField(max_length=20, null=True)
	#date = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.fname

# Create your models here.
