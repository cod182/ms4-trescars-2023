# Generated by Django 4.0 on 2022-01-10 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0009_alter_vehicle_gearbox_alter_vehicleimages_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vehicleimages',
            name='vehicle_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle'),
        ),
    ]
