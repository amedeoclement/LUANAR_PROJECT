# Generated by Django 5.0.1 on 2024-04-29 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luanarapp', '0013_calendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicstaff',
            name='department_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='luanarapp.department'),
        ),
        migrations.AlterField(
            model_name='administrationstaff',
            name='staff_position',
            field=models.CharField(choices=[('Vice Chancellor', 'Vice chancellor'), ('Deputy Vice Chancellor', 'Deputy Vice Chancellor'), ('University Registrar', 'University Registrar'), ('Dean of Students Affairs', 'Dean of Students Affairs')], max_length=100),
        ),
    ]
