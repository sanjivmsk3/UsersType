# Generated by Django 3.2.8 on 2021-10-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_categories_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='allow',
            field=models.BooleanField(default=False),
        ),
    ]
