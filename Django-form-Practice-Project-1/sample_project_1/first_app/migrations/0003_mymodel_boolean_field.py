# Generated by Django 5.0 on 2023-12-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_mymodel_date_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='boolean_field',
            field=models.BooleanField(default=False),
        ),
    ]