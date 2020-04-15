from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

class BaseFunctionalTest(LiveServerTestCase):

    # ran at start of every test
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver',chrome_options=chrome_options)

    # ran at end of every test
    def tearDown(self):
        self.browser.close()




