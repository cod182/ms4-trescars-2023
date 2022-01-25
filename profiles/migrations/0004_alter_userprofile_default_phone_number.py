# Generated by Django 4.0 on 2022-01-25 14:43

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_userprofile_default_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
