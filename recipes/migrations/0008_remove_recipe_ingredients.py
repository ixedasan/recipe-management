# Generated by Django 5.0.4 on 2024-04-20 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_recipe_ingredients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
    ]
