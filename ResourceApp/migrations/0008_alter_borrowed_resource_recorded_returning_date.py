# Generated by Django 3.2.9 on 2021-11-15 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceApp', '0007_alter_borrowed_resource_recorded_returning_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed_resource',
            name='recorded_returning_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 15, 13, 32, 15, 157860)),
        ),
    ]