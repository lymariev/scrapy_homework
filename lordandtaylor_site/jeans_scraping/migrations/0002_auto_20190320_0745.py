# Generated by Django 2.1.7 on 2019-03-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeans_scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garment',
            name='price',
            field=models.FloatField(),
        ),
    ]
