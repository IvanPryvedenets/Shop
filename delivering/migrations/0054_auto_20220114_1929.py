# Generated by Django 3.0.6 on 2022-01-14 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0053_auto_20220114_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
