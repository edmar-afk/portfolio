# Generated by Django 4.1.7 on 2023-03-31 23:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0006_remove_counterhaha_user_remove_counterheart_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 31, 23, 15, 26, 859033, tzinfo=datetime.timezone.utc), verbose_name='date commented'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='profile_pic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
