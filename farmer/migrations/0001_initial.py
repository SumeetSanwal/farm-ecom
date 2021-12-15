# Generated by Django 3.1.3 on 2020-11-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=30)),
                ('seller', models.CharField(max_length=30)),
                ('prodname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='pics')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
