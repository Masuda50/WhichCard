from django.test import TestCase
from django.urls import resolve, reverse
from .. import views


class TestUrls(TestCase):

    def test_home_url_is_resolved(self):
        self.__resolveUrl(reverse('cards:index'), views.index)

    def test_forms_url_is_resolved(self):
        self.__resolveUrl(reverse('cards:forms'), views.get_info)

    def test_aboutUs_url_is_resolved(self):
        self.__resolveUrl(reverse('cards:aboutus'), views.about_us)

    def test_displayCards_url_is_resolved(self):
        self.__resolveUrl(reverse('cards:display_cards'), views.get_display_cards)

    # helper to check if url is resolved using function
    def __resolveUrl(self, url, function):
        assert url is not None and not url.isspace()
        assert function is not None and not url.isspace()

        return self.assertEqual(resolve(url).func, function)
