from django.test import TestCase, Client
from django.urls import reverse


class CardsViewsTests(TestCase):

    # create variables on start of tests
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('cards:index')
        self.about_us_url = reverse('cards:aboutus')
        self.display_cards_url = reverse('cards:display_cards')
        self.get_info_url = reverse('cards:forms')
        self.submit_feedback_url = reverse('cards:submit_feedback')

    # test home page view
    def test_home_view_GET(self):
        response = self.__getResponse(self.home_url)
        self.__check_response_code(response)
        self.__checkTemplateUsed(response, 'cards/index.html')

    # test about us view
    def test_aboutus_view_GET(self):
        response = self.__getResponse(self.about_us_url)
        self.__check_response_code(response)
        self.__checkTemplateUsed(response, 'cards/AboutUs.html')

    # test display_card view
    def test_display_card_view_GET(self):
        response = self.__getResponse(self.display_cards_url)
        self.__check_response_code(response)
        self.__checkTemplateUsed(response, 'cards/display_cards.html')

    # test get_info view GET request
    def test_get_info_view_GET(self):
        response = self.__getResponse(self.get_info_url)
        self.__check_response_code(response)
        self.__checkTemplateUsed(response, 'cards/forms.html')

    # test get_info view given data
    def test_get_info_view_data_POST(self):
        data = {
            'groceries': 3,
            'gas': 3,
            'travels': 3,
            'clothes': 3,
            'etc': 3,
            'credit_score': 'good',
            'annual': 'yes',
            'banks': 'all',
        }

        response = self.client.post(self.get_info_url, data)

        self.__check_response_code(response)
        self.__checkTemplateUsed(response, 'cards/forms.html')

    def test_submit_feedback_view_GET(self):
        response = self.__getResponse(self.submit_feedback_url)
        self.__check_response_code(response)
        self.__checkTemplateUsed(response, 'cards/submit_feedback.html')

    # test get_info view given no data
    def test_get_info_view_no_data_POST(self):
        response = self.client.post(self.get_info_url, {})
        self.assertNotEqual(response, 302)

    # helper method to get response given view_name
    def __getResponse(self, view_name):
        assert view_name is not None and not view_name.isspace()
        return self.client.get(view_name)

    # helper to check for http response is good, i.e 200 or accurately returns false
    def __check_response_code(self, response, status_code=200):
        assert response is not None and status_code is not None

        return self.assertEqual(response.status_code, status_code)

    # helper to check if response used template
    def __checkTemplateUsed(self, response, template):
        assert response is not None
        assert template is not None and not template.isspace()

        return self.assertTemplateUsed(response, template)


