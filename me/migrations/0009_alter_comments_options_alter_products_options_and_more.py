# Generated by Django 4.2.3 on 2023-08-06 03:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0008_products_alter_comments_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Product'},
        ),
        migrations.AddField(
            model_name='products',
            name='tag',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 3, 52, 14, 726617, tzinfo=datetime.timezone.utc), verbose_name='date commented'),
        ),
    ]