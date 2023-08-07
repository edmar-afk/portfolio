# Generated by Django 4.1.7 on 2023-03-31 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0005_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counterhaha',
            name='user',
        ),
        migrations.RemoveField(
            model_name='counterheart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='countersad',
            name='user',
        ),
        migrations.RemoveField(
            model_name='counterwow',
            name='user',
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 31, 12, 46, 24, 930418, tzinfo=datetime.timezone.utc), verbose_name='date commented'),
        ),
        migrations.DeleteModel(
            name='CounterAngry',
        ),
        migrations.DeleteModel(
            name='CounterHaha',
        ),
        migrations.DeleteModel(
            name='CounterHeart',
        ),
        migrations.DeleteModel(
            name='CounterSad',
        ),
        migrations.DeleteModel(
            name='CounterWow',
        ),
    ]
