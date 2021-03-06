from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Hero

class HeroCreateView(LoginRequiredMixin, CreateView):
    model = Hero
    template_name = 'hero_add.html'
    fields = ['name', 'identity', 'description', 'image', 'strength', 'weakness']

class HeroView(RedirectView):
    url = '/hero/'

class HeroListView(ListView):
    template_name = 'hero_list.html'
    model = Hero

class HeroDetailView(DetailView):
    template_name = "hero_detail.html"
    model = Hero

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero_edit.html"
    model = Hero
    fields = ['name', 'identity', 'description', 'image', 'strength', 'weakness']

class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Hero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('hero_list')