from django.urls import reverse
from .base_test_class import BaseFunctionalTest
from cards.models import Card
import time


class TestFormPage(BaseFunctionalTest):

    def setUp(self):
        super().setUp()
        self.card = Card(
            cardName="Chase Freedom",
            bankName="Chase Bank",
            annualFee=0,
            rewardsType="Cash Back",
            rewardValue=0.01,
            rewardsDisplay="5% cash back on select categories",
            groceryMultiplier=2,
            restMultiplier=2,
            travelMultiplier=2,
            gasMultiplier=2,
            elseMultiplier=1,
            APR=2,
            bonusDisplay="dd",
            bonusValue=2,
            link="Chase.com",
            creditScore=2)

        self.card.save()
        self.browser.get(self.live_server_url + reverse("cards:forms"))

    # test valid data in form submit redirects to display_cards page
    def test_form_valid_data_submit(self):
        self.__check_form_data_submit_helper(1000)
        self.__check_valid_form_results_populated()

    # test no data in form submit stays in forms page
    def test_form_no_data_submit(self):
        self.__submit_form()
        self.__check_form_submit_redirection()

    # test invalid data in form submit stats in forms page
    def test_form_invalid_data_submit(self):
        self.__check_form_data_submit_helper('test')

    # helper to input data and redirect for form
    def __check_form_data_submit_helper(self, data):
        assert data is not None

        text_boxes = [field.find_element_by_tag_name("input") for field in
                      self.browser.find_elements_by_class_name("controls")]

        for textbox in text_boxes:
            textbox.send_keys(data)
            time.sleep(0.5)

        self.__submit_form()
        time.sleep(2)
        self.__check_form_submit_redirection()

    # find submit button and submit form
    def __submit_form(self):
        self.browser.find_element_by_tag_name("form").submit()

    # check submit form page redirection
    def __check_form_submit_redirection(self):
        self.assertEquals(self.browser.current_url,
                          self.live_server_url + reverse('cards:forms'))

    # check valid form populates results on  the page
    def __check_valid_form_results_populated(self):
        container = self.browser.find_elements_by_class_name("container")
        self.assertLess(1, len(container))

