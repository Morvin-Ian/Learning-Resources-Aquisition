# Generated by Django 4.0.4 on 2022-05-08 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DarajaApp', '0003_remove_transactiondetails_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaCallBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_request_id', models.CharField(max_length=50)),
                ('checkout_request_id', models.CharField(max_length=50)),
                ('response_code', models.CharField(max_length=50)),
                ('response_description', models.CharField(max_length=50)),
                ('customer_message', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'MpesaCallBack',
                'verbose_name_plural': 'MpesaCallBacks',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='LNMOnline',
        ),
        migrations.DeleteModel(
            name='TransactionDetails',
        ),
    ]
