from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestHomePage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    # test that the homepage was loaded
    def test_user_sees_homepage(self):
        self.browser.get(self.live_server_url)

        landing = self.browser.find_element_by_tag_name('body')

        self.assertEqual(
            landing.text, 'Which Card\nAbout Us Forms Home'
        )

    def test_home_page_redirects_to_form(self):
        self.browser.get(self.live_server_url)

        add_url = self.live_server_url
        target = self.browser.find_element_by_tag_name('a')
        print(target.text)
        time.sleep(10)
