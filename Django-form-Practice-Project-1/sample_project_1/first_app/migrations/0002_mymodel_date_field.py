# Generated by Django 5.0 on 2023-12-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='date_field',
            field=models.DateField(default=12),
        ),
    ]
