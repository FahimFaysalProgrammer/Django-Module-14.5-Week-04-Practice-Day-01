# Generated by Django 5.0 on 2023-12-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0011_mymodel_duration_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='float_field',
            field=models.FloatField(default=0.0),
        ),
    ]
