# Generated by Django 3.2.9 on 2021-11-10 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed_resource',
            name='recorded_returning_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 13, 50, 42, 245225)),
        ),
    ]
