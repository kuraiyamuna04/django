# Generated by Django 4.1.4 on 2022-12-18 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_contact_contact_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact_data',
        ),
    ]
