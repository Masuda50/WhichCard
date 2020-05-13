from django.urls import reverse
from .base_test_class import BaseFunctionalTest
import time


class TestSubmitFeedbackPage(BaseFunctionalTest):
    def setUp(self):
        super().setUp()
        self.browser.get(self.live_server_url+ reverse("cards:submit_feedback"))

    def test_valid_feedback(self):
        fields = {
            "body":
                {
                    "xpath": '// *[ @ id = "id_body"]',
                    "data": "test body",
                },
            "subject":
                {
                    "xpath": '//*[@id="id_subject"]',
                    "data": "test"
                },
            "select_issue":
                {
                    "xpath": '//*[@id="id_category_1"]',
                    "data": None,
                },
            "email":
                {
                    "xpath": '//*[@id="id_email"]',
                    "data": "test@email.com",
                },
            "name":
                {
                    "xpath": '//*[@id="id_name"]',
                    "data": "Bob Billy"
                }
        }
        for key in fields.keys():
            element = self.browser.find_element_by_xpath(fields[key]["xpath"])
            if fields[key]["data"] is None:
                element.click()
            else:
                element.send_keys(fields[key]["data"])
                time.sleep(2)
        self.browser.find_element_by_tag_name("form").submit()
        self.assertEquals(self.browser.current_url, self.live_server_url + reverse("cards:submit_feedback"))
