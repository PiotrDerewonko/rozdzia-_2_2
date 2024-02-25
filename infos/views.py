from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    t = loader.get_template("infos/main.html")
    c = {'title': 'Homepage', 'active_tab': 'home'}
    return HttpResponse(t.render(c))
