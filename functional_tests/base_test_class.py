from django.test import LiveServerTestCase
from selenium import webdriver


class BaseFunctionalTest(LiveServerTestCase):

    # ran at start of every test
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver')

    # ran at end of every test
    def tearDown(self):
        self.browser.close()




