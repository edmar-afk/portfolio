# Generated by Django 4.2.3 on 2023-08-07 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0023_alter_comments_date_alter_comments_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 7, 12, 30, 10, 363453, tzinfo=datetime.timezone.utc), verbose_name='date commented'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
