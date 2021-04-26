from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from ronanprod.views import Mainpage
from django.urls import resolve
from ronanprod.models import Item

class IndexTest(TestCase):

	def html_mainpage(self):
		found = resolve('/')
		self.assertEqual(found.func, Mainpage)

		
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
		self.assertIn('<body style="background: lightgrey; ">', html)
		self.assertIn('<div class="container">', html)
		self.assertIn('<h1 style="color: brown; font-family: Times New Roman, Times, serif; font-size: 50px; text-shadow: 2px 2px black">Sign Up</h1>', html)
		self.assertIn('<p>Please fill in this form to create an account.</p>', html)
		self.assertIn('<hr>', html)
		self.assertIn('<form class ="form" action="" method="post">', html)
		self.assertIn('<label id="firstname"><b style="color: maroon; text-shadow: 1px 1px black; font-size: 25px;">First Name:</b></label><br>', html)
		self.assertIn('<input style="width: 15cm;"type="text" id="fname" placeholder="First Name" name="fname" required><br><br>', html)
		self.assertIn('<label id="middlename"><b style="color: maroon; text-shadow: 1px 1px black; font-size: 25px;">Middle Name:</b></label><br>', html)
		self.assertIn('<input style="width: 15cm;"type="text" id="mname" placeholder="Middle Name" name="mname"><br><br>', html)
		self.assertIn('<label id="lastname"><b style="color: maroon; text-shadow: 1px 1px black; font-size: 25px;">Last Name:</b></label><br>', html)
		self.assertIn('<input style="width: 15cm;"type="text" id="lname" placeholder="Last Name" name="lname" required><br><br>', html)
		self.assertIn('<label id="extensionname"><b style="color: maroon; text-shadow: 1px 1px black; font-size: 25px;">Extension Name:</b></label><br>', html)
		self.assertIn('<input style="width: 15cm;"type="text" id="ename" placeholder="(Sr., Jr., III)" name="ename"><br><br>', html)
		self.assertIn('<label id="email"><b style="color: maroon; text-shadow: 1px 1px black; font-size: 25px;">Email:</b></label><br>', html)
		self.assertIn('<input style="width: 15cm;"type="text" id="emails" placeholder="Enter" name="emails" required><br><br>', html)
		self.assertIn('<label id="password"><b style="color: maroon; text-shadow: 1px 1px black; font-size: 25px;">Password:</b></label><br>', html)
		self.assertIn('<input style="width: 15cm;"type="password" id="password1" placeholder="New Password" name="password1" required><br><br>', html)
		self.assertIn('<label id="gender1"><b style="color: maroon; text-shadow: 1px 1px black; font-size: 25px;">Gender:</b></label>', html)
		self.assertIn('<select id="gender" name="gender">', html)
		self.assertIn('<option value="Custom" name="custom1" id="custom1">Custom</option>', html)
		self.assertIn('<option value="Male" name="male1" id="male1">Male</option>', html)
		self.assertIn('<option value="Female" name="female1" id="female1">Female</option>', html)
		self.assertIn('</select><br><br>', html)
		self.assertIn('<input type="button" class="cancelbtn" value="Cancel" id="submit" name="submit" style="color: red;">', html)
		self.assertIn('<input type="submit" class="signupbtn" value="Sign Up" id="submit1" name="submit1" style="color: black;">', html)
		self.assertIn('</form>', html)
		self.assertIn('</div>', html)
		self.assertIn('</body>', html)
		self.assertIn('</html>', html)
		self.assertTrue(html.strip().endswith('</html>'))

		self.assertTrue(html.strip().endswith('</html>'))

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

class Views(TestCase):
	def test(self):
		Item.objects.create(fname='fname', mname='mname', lname='lname', ename='ename', email='email', password='password', gender='gender')
		response = self.client.get('/app/views.Mainpage/')
