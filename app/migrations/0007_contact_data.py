# Generated by Django 4.1.4 on 2022-12-18 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_contact_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('mail', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]
