# Generated by Django 4.2.3 on 2023-08-06 03:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0009_alter_comments_options_alter_products_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='priceUsd',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 3, 53, 15, 520180, tzinfo=datetime.timezone.utc), verbose_name='date commented'),
        ),
    ]
