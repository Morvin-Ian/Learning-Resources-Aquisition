# Generated by Django 3.2.9 on 2021-11-15 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DarajaApp', '0002_lnmonline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactiondetails',
            name='phone',
        ),
    ]
