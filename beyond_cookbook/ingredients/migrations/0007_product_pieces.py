# Generated by Django 2.2 on 2020-02-10 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0006_auto_20200210_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pieces',
            field=models.SmallIntegerField(default=0),
        ),
    ]
