from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'one_page/index.html'