from django.test import TestCase
from django.test import TestCase
from django.urls import reverse

from .models import Hero


class HeroCRUDTest(TestCase):

    def test_django(self):
        print("11")
        self.assertTrue

    def test_num_hero(self):
        print("10")
        self.assertEqual(len(Hero.objects.all()), 0)

    def test_add_hero(self):
        print("9")
        Hero.objects.create(name='Wolverine', identity='Logan Howlett')
        Hero.objects.create(name='SpiderMan', identity='Peter Parker')
        self.assertEqual(len(Hero.objects.all()), 2)


    def test_hero_title(self):
        print("8")
        Hero.objects.create(name='Wolverine', identity='Logan Howlett')
        h = Hero.objects.get(pk=1)
        self.assertEqual(h.name, 'Wolverine')
        self.assertEqual(h.identity, 'Logan Howlett')
        self.assertEqual(h.description, '')

    #Test 7 will fail if run and is not run, intentionally
    def test_hero_edit(self):
        print("7")
        Hero.objects.create(name='Wolverine', identity='Logan Howlett')
        h = Hero.objects.get(pk=1)
        h.name = 'Mark Seaman'
        h.save()
        self.assertEqual(h.name, 'Wolverine')
        self.assertEqual(h.identity, 'Logan Howlett')

    def test_hero_edit(self):
        print("6")
        Hero.objects.create(name='Wolverine', identity='Logan Howlett')
        h = Hero.objects.get(pk=1)
        h.delete()
        self.assertEqual(len(Hero.objects.all()), 0)

    def test_string_representation(self):
        print("5")
        hero = Hero.objects.create(name='Wolverine', identity='Logan Howlett')
        self.assertEqual(
            str(hero), '1 - Wolverine AKA Logan Howlett')
        


class HeroViewsTest(TestCase):

    def test_home(self):
        print("4")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_get_absolute_url(self):
        print("3")
        hero = Hero.objects.create(name='Wolverine', identity='Logan Howlett')
        self.assertEqual(hero.get_absolute_url(), '/hero/1')

    #Test 2 will fail if run
    def test_hero_list_view(self):
        print("2")
        response = self.client.get(reverse('hero_list'))
        self.assertEqual(response.status_code, 200)

    def test_hero_list_view(self):
        print("1")
        response = self.client.get('/hero/')
        self.assertTemplateUsed(response, 'hero_list.html')
        self.assertTemplateUsed(response, 'superhero_theme.html')