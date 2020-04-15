from django.urls import reverse
from .base_test_class import BaseFunctionalTest
import time


class TestFormPage(BaseFunctionalTest):

    def setUp(self):
        super().setUp()
        self.browser.get(self.live_server_url + reverse("cards:forms"))

    # test valid data in form submit redirects to display_cards page
    def test_form_valid_data_submit(self):
        self.__check_form_submit_helper(3, "cards:forms")

    # test no data in form submit stays in forms page
    def test_form_no_data_submit(self):
        self.browser.find_element_by_xpath("//input[@value='Submit']").submit()

        self.assertEquals(self.browser.current_url,
                          self.live_server_url + reverse("cards:forms"))

    # test invalid data in form submit stats in forms page
    def test_form_invalid_data_submit(self):
        self.__check_form_submit_helper('test', "cards:forms")

    # helper to input data and redirect for form
    def __check_form_submit_helper(self, data, redirect_path):
        assert data is not None and redirect_path is not None

        text_boxes = [field.find_element_by_tag_name("input") for field in
                      self.browser.find_elements_by_class_name("controls")]

        for textbox in text_boxes:
            textbox.send_keys(data)
            time.sleep(0.5)

        self.browser.find_element_by_xpath("//input[@value='Submit']").submit()

        self.assertEquals(self.browser.current_url,
                          self.live_server_url + reverse(redirect_path))