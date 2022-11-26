# Generated by Django 4.0.3 on 2022-05-20 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_remove_orders_order_id_alter_orders_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_num',
            field=models.IntegerField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 20, 17, 50, 58, 657316)),
        ),
    ]
