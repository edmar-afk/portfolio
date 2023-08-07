# Generated by Django 4.2.3 on 2023-08-06 05:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0013_products_status_alter_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='file',
            field=models.FileField(default=1, upload_to='files/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 5, 33, 32, 432365, tzinfo=datetime.timezone.utc), verbose_name='date commented'),
        ),
    ]