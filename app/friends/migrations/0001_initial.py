# Generated by Django 2.0.7 on 2018-12-09 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FriendshipRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='friendshiprequest',
            unique_together={('from_user', 'to_user')},
        ),
    ]
