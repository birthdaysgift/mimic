# Generated by Django 2.0.7 on 2018-12-09 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20181208_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uservideo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='uservideo',
            name='video',
        ),
        migrations.RemoveField(
            model_name='videodislike',
            name='user',
        ),
        migrations.RemoveField(
            model_name='videodislike',
            name='uservideo',
        ),
        migrations.RemoveField(
            model_name='videolike',
            name='user',
        ),
        migrations.RemoveField(
            model_name='videolike',
            name='uservideo',
        ),
        migrations.DeleteModel(
            name='UserVideo',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.DeleteModel(
            name='VideoDislike',
        ),
        migrations.DeleteModel(
            name='VideoLike',
        ),
    ]
