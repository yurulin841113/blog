# Generated by Django 3.1.4 on 2020-12-04 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='map',
            field=models.URLField(blank=True),
        ),
    ]
