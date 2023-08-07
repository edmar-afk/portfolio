# Generated by Django 4.2.3 on 2023-08-06 04:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0010_products_priceusd_alter_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='downloads',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 4, 56, 19, 68467, tzinfo=datetime.timezone.utc), verbose_name='date commented'),
        ),
    ]