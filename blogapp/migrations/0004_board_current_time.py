# Generated by Django 4.0.7 on 2022-09-23 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_remove_board_writer_board_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='current_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
    ]
