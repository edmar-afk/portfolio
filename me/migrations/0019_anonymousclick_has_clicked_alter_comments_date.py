# Generated by Django 4.2.3 on 2023-08-06 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0018_anonymousclick_delete_click_alter_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymousclick',
            name='has_clicked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 14, 11, 59, 384169, tzinfo=datetime.timezone.utc), verbose_name='date commented'),
        ),
    ]