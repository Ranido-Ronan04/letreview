from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from ronanprod.views import Mainpage
from ronanprod.views import Page
from django.urls import resolve
#For Models testing
from ronanprod.models import Item, User
from django.urls import reverse

class IndexTest(TestCase):

	def html_mainpage(self):
		found = resolve('/')
		self.assertEqual(found.func, Mainpage)
		self.assertEqual(found.func, Page)

	def test_index_returns_correct_view(self):
		request = HttpRequest()
		response = Mainpage(request)
		html = response.content.decode('UTF-8')
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'Mainpage.html')

		self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response, 'Mainpage.html')
		self.assertIn('<title>LET REVIEWER CENTER</title>', html)

		self.assertTemplateUsed(response, 'Mainpage.html')
		self.assertIn('<html>', html)
		self.assertIn('<title>LET REVIEWER CENTER</title>', html)
		self.assertIn('<body style="background-image: linear-gradient(90deg, #43cea2, #185a9d)">', html)
		self.assertIn('<div class="container">', html)
		self.assertIn('<h1 style="color: brown; font-family: Times New Roman, Times, serif; font-size: 50px; text-shadow: 2px 2px black">Sign Up</h1>', html)
		self.assertIn('<p>Please fill in this form to create an account.</p>', html)
		self.assertIn('<hr>', html)
		self.assertIn('<form class ="form" action="" method="post">', html)
		self.assertIn('<label id="firstname"><b style="color: maroon; text-shadow: 1px 1px black; font-size: 25px;">First Name:</b></label><br>', html)
		self.assertIn('<input style="width: 15cm; background-color: lightgray; font-family: Times New Roman, Times, serif;"type="text" id="fname" placeholder="First Name" name="fname" required><br><br>', html)
		self.assertIn('<label id="middlename"><b style="color: maroon; text-shadow: 1px 1px black; font-size: 25px;">Middle Name:</b></label><br>', html)
		self.assertIn('<input style="width: 15cm; background-color: lightgray; font-family: Times New Roman, Times, serif;"type="text" id="mname" placeholder="Middle Name" name="mname"><br><br>', html)
		self.assertIn('<label id="lastname"><b style="color: maroon; text-shadow: 1px 1px black; font-size: 25px;">Last Name:</b></label><br>', html)
		self.assertIn('<input style="width: 15cm; background-color: lightgray; font-family: Times New Roman, Times, serif;"type="text" id="lname" placeholder="Last Name" name="lname" required><br><br>', html)
		self.assertIn('<label id="extensionname"><b style="color: maroon; text-shadow: 1px 1px black; font-size: 25px;">Extension Name:</b></label><br>', html)
		self.assertIn('<input style="width: 15cm; background-color: lightgray; font-family: Times New Roman, Times, serif;"type="text" id="ename" placeholder="(Sr., Jr., III)" name="ename"><br><br>', html)
		self.assertIn('<label id="email"><b style="color: maroon; text-shadow: 1px 1px black; font-size: 25px;">Email:</b></label><br>', html)
		self.assertIn('<input style="width: 15cm; background-color: lightgray; font-family: Times New Roman, Times, serif;"type="text" id="emails" placeholder="Enter" name="emails" required><br><br>', html)
		self.assertIn('<label id="password"><b style="color: maroon; text-shadow: 1px 1px black; font-size: 25px;">Password:</b></label><br>', html)
		self.assertIn('<input style="width: 15cm; background-color: lightgray; font-family: Times New Roman, Times, serif;"type="password" id="password1" placeholder="New Password" name="password1" required><br><br>', html)
		self.assertIn('<label id="gender1"><b style="color: maroon; text-shadow: 1px 1px black; font-size: 25px;">Gender:</b></label>', html)
		self.assertIn('<select id="gender" name="gender">', html)
		self.assertIn('<option value="Custom" name="custom1" id="custom1" style="font-family: Arial, Helvetica, sans-serif;">Custom</option>', html)
		self.assertIn('<option value="Male" name="male1" id="male1" style="font-family: Arial, Helvetica, sans-serif;">Male</option>', html)
		self.assertIn('<option value="Female" name="female1" id="female1" style="font-family: Arial, Helvetica, sans-serif;">Female</option>', html)
		self.assertIn('</select><br><br>', html)
		self.assertIn('<input type="button" class="cancelbtn" value="Cancel" id="submit" name="submit" style="color: red;">', html)
		self.assertIn('<input type="submit" class="signupbtn" value="Sign Up" id="submit1" name="submit1" style="color: black;">', html)
		self.assertIn('</form>', html)
		self.assertIn('</div>', html)
		self.assertIn('</body>', html)
		self.assertIn('</html>', html)
		self.assertTrue(html.strip().endswith('</html>'))

		#self.assertTrue(html.strip().endswith('</html>'))

class ListViewTest(TestCase):

	def test_uses_list_template(self):
		collab = User.objects.create()
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'Mainpage.html')
	def test_uses_home_template(self):
		response = self.client.get('/next/')
		#self.assertTemplateUsed(response, 'mainpage1.html')
	def test_displays_all_list_items(self):
		collab = User.objects.create()
		fname = Item.objects.create(fname='fname')
		mname = Item.objects.create(mname='mname')
		lname = Item.objects.create(lname='lname')
		ename = Item.objects.create(ename='ename')
		email = Item.objects.create(email='email')
		password = Item.objects.create(password='password')
		gender = Item.objects.create(gender='gender')
		response = self.client.get('/')
		self.assertIn('fname', response.content.decode())
		self.assertIn('mname', response.content.decode())
		self.assertIn('lname', response.content.decode())
		self.assertIn('ename', response.content.decode())
		self.assertIn('email', response.content.decode())
		self.assertIn('password', response.content.decode())
		self.assertIn('gender', response.content.decode())
		fname = Item.objects.get(fname="fname")
		mname = Item.objects.get(mname="mname")
		lname = Item.objects.get(lname="lname")
		ename = Item.objects.get(ename="ename")
		email = Item.objects.get(email="email")
		password = Item.objects.get(password="password")
		gender = Item.objects.get(gender="gender")
		self.assertEqual(Item.objects.count(), 7)

class ORM_save_item1(TestCase):
	def test_saving_ronan(self):
		Item1 = Item()
		Item1.fname = 'Juan'
		Item1.save()
		Item2 = Item()
		Item2.mname = 'Gomez'
		Item2.save()
		Item3 = Item()
		Item3.lname = 'Dela Cruz'
		Item3.save()
		Item4 = Item()
		Item4.ename = 'Jr.'
		Item4.save()
		Item5 = Item()
		Item5.email = 'juan.delacruz@yahoo.com'
		Item5.save()
		Item6 = Item()
		Item6.password = '123456'
		Item6.save()
		Item7 = Item()
		Item7.gender = 'Male'
		Item7.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 7)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		save6 = saveall[5]
		save7 = saveall[6]
		self.assertEqual(Item1.fname, 'Juan')
		self.assertEqual(Item2.mname, 'Gomez')
		self.assertEqual(Item3.lname, 'Dela Cruz')
		self.assertEqual(Item4.ename, 'Jr.')
		self.assertEqual(Item5.email, 'juan.delacruz@yahoo.com')
		self.assertEqual(Item6.password, '123456')
		self.assertEqual(Item7.gender, 'Male')

class ORM_save_item2(TestCase):
	def test_saving_ronan(self):
		Item1 = Item()
		Item1.fname = 'Ronan Kyle'
		Item1.save()
		Item2 = Item()
		Item2.mname = ''
		Item2.save()
		Item3 = Item()
		Item3.lname = 'Ranido'
		Item3.save()
		Item4 = Item()
		Item4.ename = ''
		Item4.save()
		Item5 = Item()
		Item5.email = 'ronankyle.ranido@gsfe.tupcavite.edu.ph'
		Item5.save()
		Item6 = Item()
		Item6.password = 'ronankyle'
		Item6.save()
		Item7 = Item()
		Item7.gender = 'Male'
		Item7.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 7)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		save6 = saveall[5]
		save7 = saveall[6]
		self.assertEqual(Item1.fname, 'Ronan Kyle')
		self.assertEqual(Item2.mname, '')
		self.assertEqual(Item3.lname, 'Ranido')
		self.assertEqual(Item4.ename, '')
		self.assertEqual(Item5.email, 'ronankyle.ranido@gsfe.tupcavite.edu.ph')
		self.assertEqual(Item6.password, 'ronankyle')
		self.assertEqual(Item7.gender, 'Male')

# class Views(TestCase):
# 	def test(self):
# 		Item.objects.create(fname='fname', mname='mname', lname='lname', ename='ename', email='email', password='password', gender='gender')
# 		response = self.client.get('/app/views.Mainpage/')

class Views(TestCase):
	def setUp(self):
		fname = Item.objects.create()
		mnane = Item.objects.create()
		lname = Item.objects.create()
		ename = Item.objects.create()
		email = Item.objects.create()
		password = Item.objects.create()
		gender = Item.objects.create()
		
		Item.objects.create(
			fname = 'Juan',
			mname = 'Gomez',
			lname = 'Dela Cruz',
			ename = 'Jr.',
			email = 'juan.delacruz@yahoo.com',
			password = '123456',
			gender = 'Male',
			)
		self.client.post('oks')
		self.assertEqual(Item.objects.count(), 8)
		

	def test_redirect_view(self):
		fname = Item.objects.get(fname="Juan")
		mname = Item.objects.get(mname="Gomez")
		lname = Item.objects.get(lname="Dela Cruz")
		ename = Item.objects.get(ename="Jr.")
		email = Item.objects.get(email="juan.delacruz@yahoo.com")
		password = Item.objects.get(password="123456")
		gender = Item.objects.get(gender="Male")

		# response = self.client.post('oks')
		# self.assertRedirects(response, 'oks')
class Models(TestCase):

	def modelo(self, 
		fname="Juan", 
		mname="Gomez", 
		lname="Dela Cruz", 
		ename="Jr.", 
		email="juan.delacruz@yahoo.com", 
		password="123456", 
		gender="Male"):
		
		return User.objects.create()
		return Item.objects.create(
			fname="fname", 
			mname="mname", 
			lname="lname", 
			ename="ename", 
			email="email", 
			password="password", 
			gender="gender", )

	def test_whatever_creation(self):
		w = self.modelo()
		self.assertTrue(isinstance(w, User))
		self.assertFalse(isinstance(w, Item))
