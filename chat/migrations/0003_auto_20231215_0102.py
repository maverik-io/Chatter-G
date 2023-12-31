# Generated by Django 3.2.13 on 2023-12-15 01:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_room_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_code',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_name',
        ),
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='message',
            name='value',
            field=models.CharField(default='TEST', max_length=1000000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='TEST', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=1000000),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=1000000),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
