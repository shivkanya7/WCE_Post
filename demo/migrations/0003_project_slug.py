# Generated by Django 3.2 on 2021-05-04 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_project_tag_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
