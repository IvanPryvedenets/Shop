# Generated by Django 3.0.4 on 2020-03-26 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('taste', models.CharField(blank=True, max_length=50)),
                ('topping', models.CharField(blank=True, max_length=50)),
                ('glaze', models.CharField(blank=True, max_length=50)),
                ('milk', models.CharField(blank=True, max_length=10)),
                ('pollination', models.CharField(blank=True, max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('number', models.IntegerField(default=1)),
                ('count', models.IntegerField(default=1)),
            ],
        ),
    ]
