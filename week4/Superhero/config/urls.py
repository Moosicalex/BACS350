from django.contrib import admin
from django.urls import path
from hero.views import IndexView, HeroListView, HeroDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('hero/', HeroListView.as_view()),
    path('hero/<int:pk>', HeroDetailView.as_view()),
]
