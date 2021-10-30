from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Hero

class HeroView(RedirectView):
    url = '/hero/'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class HeroListView(ListView):
    template_name = "hero_list.html"
    model = Hero 

class HeroDetailView(DetailView):
    template_name = 'hero_detail.html'
    model = Hero

class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = 'hero_add.html'
    model = Hero
    fields = ['name', 'identity', 'description', 'image', 'strength', 'weakness']

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'hero_edit.html'
    model = Hero
    fields = ['name', 'identity', 'description', 'image', 'strength', 'weakness']

class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Hero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('hero_list')
