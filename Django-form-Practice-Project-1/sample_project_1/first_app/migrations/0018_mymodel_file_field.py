# Generated by Django 5.0 on 2023-12-28 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0017_mymodel_generic_ip_address_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='file_field',
            field=models.FileField(default=None, upload_to='files/'),
        ),
    ]