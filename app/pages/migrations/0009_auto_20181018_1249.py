# Generated by Django 2.0.7 on 2018-10-18 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_uservideo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uservideo',
            old_name='photo',
            new_name='video',
        ),
    ]
