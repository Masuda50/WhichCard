from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'),
    path('forms', views.get_info, name='forms'),
    path('aboutus', views.about_us, name='aboutus')
]
