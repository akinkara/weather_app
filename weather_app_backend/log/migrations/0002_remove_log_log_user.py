# Generated by Django 3.1.7 on 2021-04-02 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='log_user',
        ),
    ]
