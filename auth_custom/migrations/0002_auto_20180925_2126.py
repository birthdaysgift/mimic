# Generated by Django 2.0.7 on 2018-09-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_custom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
