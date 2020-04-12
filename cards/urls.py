from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'),
    path('forms', views.get_info, name='forms'),
    path('display_cards', views.get_display_cards, name='display_cards'),
]
