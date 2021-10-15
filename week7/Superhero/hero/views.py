from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Hero

class HeroView(RedirectView):
    url = '/hero/'

class HeroListView(ListView):
    template_name = "hero_list.html"
    model = Hero 

class HeroDetailView(DetailView):
    template_name = 'hero_detail.html'
    model = Hero

class HeroCreateView(CreateView):
    template_name = 'hero_add.html'
    model = Hero
    fields = ['name', 'identity']

class HeroUpdateView(UpdateView):
    template_name = 'hero_edit.html'
    model = Hero
    fields = ['name', 'identity']

class HeroDeleteView(DeleteView):
    model = Hero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('book_list')
