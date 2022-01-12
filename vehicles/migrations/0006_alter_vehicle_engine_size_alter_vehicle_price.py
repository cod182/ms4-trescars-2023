# Generated by Django 4.0 on 2022-01-09 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_alter_vehicle_full_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='engine_size',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='price',
            field=models.IntegerField(default=200),
        ),
    ]
