# Generated by Django 3.0.6 on 2022-01-13 23:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0050_comment_audit'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='area',
            field=models.CharField(default=12, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='department',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='pay_way',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='transporter',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
