# Generated by Django 4.0.3 on 2022-05-07 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_category_id_alter_customer_id_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
    ]
