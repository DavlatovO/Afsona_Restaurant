# Generated by Django 5.0.6 on 2024-05-21 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menucuisine',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]