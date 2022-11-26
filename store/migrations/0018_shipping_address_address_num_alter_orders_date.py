# Generated by Django 4.0.3 on 2022-05-17 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_orders_billing_address_alter_orders_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping_address',
            name='address_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 17, 13, 4, 27, 564179)),
        ),
    ]
