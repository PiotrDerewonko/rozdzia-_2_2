from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    t = loader.get_template("infos/main.html")
    c = {'title': 'Homepage', 'active_tab': 'home'}
    return HttpResponse(t.render(c))

def about_me(request):
    t = loader.get_template("infos/about_me.html")
    c = {'title': 'O mnie', 'active_tab': 'me'}
    return HttpResponse(t.render(c))

def contact(request):
    t = loader.get_template("infos/contact.html")
    c = {'title': 'Kontakt', 'active_tab': 'contact'}
    return HttpResponse(t.render(c))
