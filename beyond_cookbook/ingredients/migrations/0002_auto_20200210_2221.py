# Generated by Django 2.2 on 2020-02-10 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20200210_2221'),
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
