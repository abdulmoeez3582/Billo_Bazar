# Generated by Django 4.0.3 on 2022-05-19 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_shipping_address_address_num_alter_orders_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shipping_Address',
            new_name='Address_Book',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 19, 19, 7, 11, 998145)),
        ),
    ]
