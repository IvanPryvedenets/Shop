# Generated by Django 3.0.4 on 2020-04-15 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0031_auto_20200415_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectedproduct',
            name='product',
            field=models.ForeignKey(default=39, on_delete=django.db.models.deletion.CASCADE, to='delivering.Product'),
            preserve_default=False,
        ),
    ]
