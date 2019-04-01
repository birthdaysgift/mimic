# Generated by Django 2.1.7 on 2019-03-31 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendship',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='user2',
        ),
        migrations.AlterUniqueTogether(
            name='friendshiprequest',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='friendshiprequest',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='friendshiprequest',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='Friendship',
        ),
        migrations.DeleteModel(
            name='FriendshipRequest',
        ),
    ]