# Generated by Django 4.2.2 on 2023-06-23 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_piece_part_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='part_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Inst1Piece', to='music.part'),
        ),
    ]
