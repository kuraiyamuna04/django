# Generated by Django 4.1.4 on 2022-12-17 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sign_up',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='sign_up',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='sign_up',
            old_name='phone_number',
            new_name='password',
        ),
    ]