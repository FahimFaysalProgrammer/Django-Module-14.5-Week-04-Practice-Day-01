# Generated by Django 5.0 on 2023-12-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0009_mymodel_big_integer_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='binary_field',
            field=models.BinaryField(default=0),
        ),
    ]
