from . import views
from django.urls import path
#
app_name = 'cards'          # used for referring to views urls

urlpatterns = [
    path('', views.home, name='home'),
    path('forms', views.get_info, name='forms'),
    path('aboutus', views.about_us, name='aboutus'),
    path('display_cards', views.get_display_cards, name='display_cards'),
]
