from django.shortcuts import render
from django.views.generic  import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'home-02.html'