# Generated by Django 4.1.1 on 2022-10-27 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_shift_time_reserved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='nurse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Shift_nurse', to='core.nurse'),
        ),
    ]
