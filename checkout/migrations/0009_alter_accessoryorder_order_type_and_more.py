# Generated by Django 4.0 on 2022-01-17 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_accessoryorderlineitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessoryorder',
            name='order_type',
            field=models.CharField(default='accessories', max_length=15),
        ),
        migrations.AlterField(
            model_name='accessoryorderlineitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessorylineitems', to='checkout.accessoryorder'),
        ),
        migrations.AlterField(
            model_name='accessoryorderlineitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
