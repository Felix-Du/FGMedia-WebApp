# Generated by Django 4.2 on 2023-04-17 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fgcomboapp', '0004_alter_combo_combonotation_alter_combo_metercost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='combo',
            name='damage',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Damage'),
        ),
    ]