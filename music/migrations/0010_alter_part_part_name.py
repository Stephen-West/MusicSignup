# Generated by Django 4.2.2 on 2023-07-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_alter_piece_piece_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='part_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
