from . import views
from django.urls import path

app_name = 'cards'

urlpatterns = [
    path('', views.index, name='index'),
    path('forms', views.get_info, name='forms'),
    path('aboutus', views.about_us, name='aboutus'),
    path('display_cards', views.get_display_cards, name='display_cards'),

]
