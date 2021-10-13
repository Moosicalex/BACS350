from django.test import TestCase
from hero.models import Hero
from django.test import TestCase
from django.urls import reverse

from .models import Hero


class HeroCRUDTest(TestCase):

    def test_django(self):
        self.assertTrue

    def test_num_hero(self):
        self.assertEqual(len(Hero.objects.all()), 0)

    def test_add_hero(self):
        Hero.objects.create(name='Wolverine', identity='Logan Howlett')
        Hero.objects.create(name='SpiderMan', identity='Peter Parker')
        self.assertEqual(len(Hero.objects.all()), 2)

    def test_hero_title(self):
        Hero.objects.create(name='Wolverine', identity='Logan Howlett')
        h = Hero.objects.get(pk=1)
        self.assertEqual(h.name, 'Wolverine')
        self.assertEqual(h.identity, 'Logan Howlett')

    def test_hero_edit(self):
        Hero.objects.create(name='Wolverine', identity='Logan Howlett')
        h = Hero.objects.get(pk=1)
        h.name = 'Mark Seaman'
        h.save()
        self.assertEqual(h.name, 'Wolverine')
        self.assertEqual(h.identity, 'Logan Howlett')

    def test_hero_edit(self):
        Hero.objects.create(name='Wolverine', identity='Logan Howlett')
        h = Hero.objects.get(pk=1)
        h.delete()
        self.assertEqual(len(Hero.objects.all()), 0)

    def test_string_representation(self):
        hero = Hero.objects.create(name='Wolverine', identity='Logan Howlett')
        self.assertEqual(
            str(hero), '1 - Wolverine AKA Logan Howlett')


class HeroViewsTest(TestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_get_absolute_url(self):
        hero = Hero.objects.create(name='Wolverine', identity='Logan Howlett')
        self.assertEqual(hero.get_absolute_url(), '/hero/1')

    def test_hero_list_view(self):
        response = self.client.get(reverse('hero_list'))
        self.assertEqual(response.status_code, 200)

    def test_hero_list_view(self):
        response = self.client.get('/hero/')
        self.assertTemplateUsed(response, 'hero_list.html')
        self.assertTemplateUsed(response, 'hero_theme.html')
