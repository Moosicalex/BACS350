from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Hero


class HeroView(ListView):
    template_name = 'hero_list.html'
    model = Hero

class HeroDetail(DetailView):
    template_name = 'hero_detail.html'
    model = Hero