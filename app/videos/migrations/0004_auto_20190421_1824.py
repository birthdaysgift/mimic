# Generated by Django 2.1.7 on 2019-04-21 18:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0003_auto_20190421_1712'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserVideo',
            new_name='PostedVideo',
        ),
    ]