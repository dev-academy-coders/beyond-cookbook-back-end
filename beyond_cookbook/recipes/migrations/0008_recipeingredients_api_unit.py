# Generated by Django 2.2 on 2020-02-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20200211_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredients',
            name='api_unit',
            field=models.IntegerField(default=1),
        ),
    ]