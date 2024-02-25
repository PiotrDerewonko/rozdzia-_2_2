
from django.urls import path
from django.views.generic import TemplateView
from.views import home

app_name = 'infos'

urlpatterns = [
    path('', home, name='home'),
    path('me', TemplateView.as_view(template_name='infos/about_me.html'), name='me'),
    path('contact', TemplateView.as_view(template_name='infos/contact.html'), name='contact'),
]