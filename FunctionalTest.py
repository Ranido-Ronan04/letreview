from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

"""browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')"""

class PageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	"""def tearDown(self):
		self.browser.quit()"""

	def test_browser_test(self):
		"""self.browser.get('http://localhost:8000')
		self.assertIn('BTS', self.browser.title)"""
		#self.fail('Finish the test!')

	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Profile', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Profile of Student', headerText)
		inputbox = self.browser.find_element_by_id('newEntry1')
		self.assertEqual(inputbox.get_attribute('placeholder'),'Student Name:')
		inputbox.send_keys('Ronan Kyle Ranido')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		inputbox = self.browser.find_element_by_id('newPlace1')
		self.assertEqual(inputbox.get_attribute('placeholder'),'Course:')
		inputbox.send_keys('BSIE - ICT - 3A')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		inputbox = self.browser.find_element_by_id('newEntry2')
		self.assertEqual(inputbox.get_attribute('placeholder'),'Student Number:')
		inputbox.send_keys('TUPC - 18 - 0092')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		
		#table = self.browser.find_element_by_id('idListTable')
		#rows = table.find_element_by_tag_name('tr')
		#self.assertTrue(any(row.text == '1:BTS'))
		#self.fail('Finish the test!')"""



if __name__ == '__main__':
    unittest.main(warnings='ignore')