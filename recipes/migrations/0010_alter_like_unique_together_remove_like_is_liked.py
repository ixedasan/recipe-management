# Generated by Django 5.0.4 on 2024-04-21 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_like_is_liked'),
        ('user', '0004_delete_follow'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('profile', 'recipe')},
        ),
        migrations.RemoveField(
            model_name='like',
            name='is_liked',
        ),
    ]
