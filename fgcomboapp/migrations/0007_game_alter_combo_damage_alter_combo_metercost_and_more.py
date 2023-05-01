# Generated by Django 4.2 on 2023-05-01 01:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fgcomboapp', '0006_combo_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Game Title')),
            ],
        ),
        migrations.AlterField(
            model_name='combo',
            name='damage',
            field=models.PositiveBigIntegerField(verbose_name='Damage'),
        ),
        migrations.AlterField(
            model_name='combo',
            name='meterCost',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)], verbose_name='Meter Cost'),
        ),
        migrations.AlterField(
            model_name='combo',
            name='meterGain',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)], verbose_name='Meter Gain'),
        ),
        migrations.AlterField(
            model_name='combo',
            name='moonSkillCost',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)], verbose_name='Moon Skill Cost'),
        ),
        migrations.AddField(
            model_name='combo',
            name='game',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='fgcomboapp.game'),
        ),
    ]
