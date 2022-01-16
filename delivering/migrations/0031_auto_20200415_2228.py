# Generated by Django 3.0.4 on 2020-04-15 19:28

from django.db import migrations, models
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0030_auto_20200415_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedproduct',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=Decimal(0), max_digits=10),
        ),
    ]
