# Generated by Django 3.2.7 on 2021-10-16 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='description',
            field=models.TextField(default='Enter Description Here'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='image',
            field=models.CharField(default='\\static\\images\\Bear.200.png', max_length=1000),
        ),
        migrations.AlterField(
            model_name='hero',
            name='strength',
            field=models.CharField(default='Enter Strength Here', max_length=100),
        ),
        migrations.AlterField(
            model_name='hero',
            name='weakness',
            field=models.CharField(default='Enter Weakness Here', max_length=100),
        ),
    ]
