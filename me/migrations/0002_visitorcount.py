# Generated by Django 4.1.7 on 2023-03-25 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
