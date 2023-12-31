# Generated by Django 4.2.3 on 2023-08-07 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0022_alter_comments_date_alter_comments_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 7, 12, 28, 24, 333344, tzinfo=datetime.timezone.utc), verbose_name='date commented'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='profile_pic',
            field=models.ImageField(default=None, null=True, upload_to='images/'),
        ),
    ]
