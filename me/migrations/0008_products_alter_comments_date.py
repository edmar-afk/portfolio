# Generated by Django 4.2.3 on 2023-08-06 03:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0007_alter_comments_date_alter_comments_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 3, 49, 48, 924077, tzinfo=datetime.timezone.utc), verbose_name='date commented'),
        ),
    ]
