# Generated by Django 4.0.7 on 2022-09-25 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0015_board_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
