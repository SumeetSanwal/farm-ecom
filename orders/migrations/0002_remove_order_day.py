# Generated by Django 3.1.3 on 2020-11-27 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='day',
        ),
    ]
