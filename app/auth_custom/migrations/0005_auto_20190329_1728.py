# Generated by Django 2.1.7 on 2019-03-29 17:28

import auth_custom.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_custom', '0004_auto_20190328_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=auth_custom.models.user_photos_path),
        ),
    ]