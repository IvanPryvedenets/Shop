# Generated by Django 3.0.4 on 2020-04-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0024_auto_20200414_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedproduct',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
