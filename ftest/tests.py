from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

class PageTest(LiveServerTestCase):

	
	def setUp(self):
		self.browser = webdriver.Firefox()
		

	def test_browser_title(self):
		self.browser.get(self.live_server_url)
		self.assertIn('LET REVIEWER CENTER', self.browser.title)

		nanText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Sign Up', nanText)

		prgrph = self.browser.find_element_by_tag_name('p').text
		self.assertIn('Please fill in this form to create an account.', prgrph)

		form = self.browser.find_element_by_tag_name('form')

		label1 = self.browser.find_element_by_id('firstname').text
		self.assertIn('First Name:', label1)

		label2 = self.browser.find_element_by_id('middlename').text
		self.assertIn('Middle Name:', label2)

		label3 = self.browser.find_element_by_id('lastname').text
		self.assertIn('Last Name:', label3)

		label4 = self.browser.find_element_by_id('extensionname').text
		self.assertIn('Extension Name:', label4)

		label5 = self.browser.find_element_by_id('email').text
		self.assertIn('Email:', label5)

		label6 = self.browser.find_element_by_id('password').text
		self.assertIn('Password:', label6)

		label7 = self.browser.find_element_by_id('gender1').text
		self.assertIn('Gender:', label7)

		input1 = self.browser.find_element_by_id('fname')  
		self.assertEqual(input1.get_attribute('placeholder'),'First Name')
		input1 = self.browser.find_element_by_id('fname').send_keys("Juan")
		time.sleep(1)

		input2 = self.browser.find_element_by_id('mname')  
		self.assertEqual(input2.get_attribute('placeholder'),'Middle Name')
		input2 = self.browser.find_element_by_id('mname').send_keys("Gomez")
		time.sleep(1)

		input3 = self.browser.find_element_by_id('lname')  
		self.assertEqual(input3.get_attribute('placeholder'),'Last Name')
		input3 = self.browser.find_element_by_id('lname').send_keys("Dela Cruz")
		time.sleep(1)
		
		input4 = self.browser.find_element_by_id('ename')  
		self.assertEqual(input4.get_attribute('placeholder'),'(Sr., Jr., III)')
		input4 = self.browser.find_element_by_id('ename').send_keys("Jr.")
		time.sleep(1)
		
		input5 = self.browser.find_element_by_id('emails')
		self.assertEqual(input5.get_attribute('placeholder'),'Enter')
		input5 = self.browser.find_element_by_id('emails').send_keys("juan.delacruz@yahoo.com")
		time.sleep(1)
		
		input6 = self.browser.find_element_by_id('password1')  
		self.assertEqual(input6.get_attribute('placeholder'),'New Password')
		input6 = self.browser.find_element_by_id('password1').send_keys("123456")
		time.sleep(1)

		#select option1
		select = self.browser.find_element_by_id('gender').click()
		time.sleep(1)
		option1 = self.browser.find_element_by_id('custom1').text
		self.assertIn('Custom', option1)
		#option1 = self.browser.find_element_by_id('custom1').send_keys("Custom")
		#select option2
		option2 = self.browser.find_element_by_id('male1').text
		self.assertIn('Male', option2)
		option2 = self.browser.find_element_by_id('male1').send_keys("Male")
		#select option3
		option3 = self.browser.find_element_by_id('female1').text
		self.assertIn('Female', option3)
		#option3 = self.browser.find_element_by_id('female1').send_keys("Female")
		time.sleep(1)
		submitbutton = self.browser.find_element_by_name('submit1').click()
		time.sleep(2)

		nextpage = self.browser.current_url
		self.assertRegex(nextpage, '/oks')

		self.browser.quit()	
		
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)

		input1 = self.browser.find_element_by_id('fname')  
		self.assertEqual(input1.get_attribute('placeholder'),'First Name')
		input1 = self.browser.find_element_by_id('fname').send_keys("Ronan Kyle")
		time.sleep(1)

		input2 = self.browser.find_element_by_id('mname')  
		self.assertEqual(input2.get_attribute('placeholder'),'Middle Name')
		input2 = self.browser.find_element_by_id('mname').send_keys("")
		time.sleep(1)

		input3 = self.browser.find_element_by_id('lname')  
		self.assertEqual(input3.get_attribute('placeholder'),'Last Name')
		input3 = self.browser.find_element_by_id('lname').send_keys("Ranido")
		time.sleep(1)
		
		input4 = self.browser.find_element_by_id('ename')  
		self.assertEqual(input4.get_attribute('placeholder'),'(Sr., Jr., III)')
		input4 = self.browser.find_element_by_id('ename').send_keys("")
		time.sleep(1)
		
		input5 = self.browser.find_element_by_id('emails')
		self.assertEqual(input5.get_attribute('placeholder'),'Enter')
		input5 = self.browser.find_element_by_id('emails').send_keys("ronankyle.ranido@gsfe.tupcavite.edu.ph")
		time.sleep(1)
		
		input6 = self.browser.find_element_by_id('password1')  
		self.assertEqual(input6.get_attribute('placeholder'),'New Password')
		input6 = self.browser.find_element_by_id('password1').send_keys("ronankyle")
		time.sleep(1)

		#select option1
		select = self.browser.find_element_by_id('gender').click()
		time.sleep(1)
		option1 = self.browser.find_element_by_id('custom1').text
		self.assertIn('Custom', option1)
		#option1 = self.browser.find_element_by_id('custom1').send_keys("Custom")
		#select option2
		option2 = self.browser.find_element_by_id('male1').text
		self.assertIn('Male', option2)
		option2 = self.browser.find_element_by_id('male1').send_keys("Male")
		#select option3
		option3 = self.browser.find_element_by_id('female1').text
		self.assertIn('Female', option3)
		#option3 = self.browser.find_element_by_id('female1').send_keys("Female")
		time.sleep(1)
		submitbutton = self.browser.find_element_by_name('submit1').click()
		time.sleep(2)

		nextpage = self.browser.current_url
		self.assertRegex(nextpage, '/oks')

		self.browser.quit()	

		
		


# if __name__ == '__main__':
# 	unittest.main()