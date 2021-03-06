# Generated by Django 2.2 on 2020-02-10 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0008_auto_20200210_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='default_quantity',
        ),
        migrations.AddField(
            model_name='product',
            name='grams_per_piece',
            field=models.DecimalField(decimal_places=9, default=0, max_digits=18),
        ),
        migrations.AddField(
            model_name='product',
            name='mililiters_per_piece',
            field=models.DecimalField(decimal_places=9, default=0, max_digits=18),
        ),
        migrations.AddField(
            model_name='product',
            name='pieces',
            field=models.SmallIntegerField(default=0),
        ),
    ]
