from django.urls import reverse
from .base_test_class import BaseFunctionalTest


class TestAboutUsPage(BaseFunctionalTest):

    def setUp(self):
        super().setUp()
        self.browser.get(self.live_server_url + reverse("cards:aboutus"))

    def test_links(self):
        for link in self.__get_all_links():
            self.__test_link(link)
            self.__browser_reset()

    def __get_all_links(self):
        return [link.get_attribute("href") for link in
                self.browser.find_element_by_class_name("container").find_elements_by_tag_name("a")]

    def __test_link(self, link_text):
        assert link_text is not None

        self.browser.find_element_by_xpath(f"//a[@href='{link_text}']").click()
        self.browser.implicitly_wait(10)
        self.assertEquals(self.browser.current_url, link_text)
        self.tearDown()

    def __browser_reset(self):
        self.setUp()
