
from django.urls import path
from.views import home, about_me, contact

app_name = 'infos'

urlpatterns = [
    path('', home, name='home'),
    path('me', about_me, name='me'),
    path('contact', contact, name='contact'),
]