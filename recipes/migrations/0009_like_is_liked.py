# Generated by Django 5.0.4 on 2024-04-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_remove_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='is_liked',
            field=models.BooleanField(default=True),
        ),
    ]