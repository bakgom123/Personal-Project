# Generated by Django 3.2.14 on 2022-07-15 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_bookmark_like_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='like_count',
        ),
    ]