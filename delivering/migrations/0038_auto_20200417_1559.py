# Generated by Django 3.0.4 on 2020-04-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0037_auto_20200417_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True),
        ),
        migrations.AlterField(
            model_name='selectedproduct',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True),
        ),
    ]
