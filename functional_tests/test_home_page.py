from django.urls import reverse
from .base_test_class import BaseFunctionalTest


class TestHomePage(BaseFunctionalTest):

    def setUp(self):
        super().setUp()
        self.browser.get(self.live_server_url)                 # home url

    # test click Forms in navbar
    def test_home_page_redirects_to_forms(self):
        self.__check_navbar_redirection_to("Forms", 'cards:forms')

    # test click About us in navbar
    def test_home_page_redirects_to_aboutus(self):
        self.__check_navbar_redirection_to("About Us", 'cards:aboutus')

    # test click Home in navbar
    def test_home_page_redirects_to_home(self):
        self.__check_navbar_redirection_to("Home\n(current)", "cards:index")
        
    # test click Submit Feedback in navbar
    def test_home_page_redirects_to_submit_feedback(self):
        self.__check_navbar_redirection_to("Submit Feedback", "cards:submit_feedback")

    # helper to test navigation bar re-directions
    def __check_navbar_redirection_to(self, element, destination):

        assert element is not None and not element.isspace()
        assert destination is not None and not destination.isspace()
        self.browser.find_element_by_tag_name('button').click()
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_link_text(element).click()

        target_url = self.live_server_url + reverse(destination)

        self.assertEquals(self.browser.current_url,
                          target_url)

