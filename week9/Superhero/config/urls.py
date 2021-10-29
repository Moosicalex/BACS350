from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.contrib import admin
from django.urls import path

from hero.views import HeroView


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    # Book
    path('', include('hero.urls')),

    # Document
    path('', include('doc.urls')),

]