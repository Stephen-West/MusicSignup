# Generated by Django 4.2.2 on 2023-07-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_part_instrument_alter_part_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='is_present',
        ),
        migrations.AddField(
            model_name='part',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]