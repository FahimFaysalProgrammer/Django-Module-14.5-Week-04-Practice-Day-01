# Generated by Django 5.0 on 2023-12-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0015_mymodel_positive_big_integer_field_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='decimal_field',
            field=models.DecimalField(decimal_places=2, default=2.8, max_digits=5),
        ),
    ]
