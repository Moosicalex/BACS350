from django.db import models
from django.urls.base import reverse_lazy

class Hero(models.Model):
    name = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    description = models.TextField(default="Enter Description Here")
    strength = models.CharField(max_length=100, default="Enter Strength Here")
    weakness = models.CharField(max_length=100, default="Enter Weakness Here")
    image = models.CharField(max_length =1000, default="\static\images\bear.200.png")

    def get_absolute_url(self):
        return reverse_lazy('hero_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.pk} - {self.name} AKA {self.identity}'