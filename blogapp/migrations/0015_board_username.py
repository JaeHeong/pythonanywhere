# Generated by Django 4.0.7 on 2022-09-25 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_fileupload_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
