# Generated by Django 3.2.5 on 2022-01-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0015_auto_20220118_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='visited',
            field=models.BooleanField(default=False),
        ),
    ]
