# Generated by Django 5.0.1 on 2024-04-01 21:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luanarapp', '0005_remove_program_level'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Prospectus',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='advert',
        ),
        migrations.AlterField(
            model_name='department',
            name='faculty_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='luanarapp.faculty'),
        ),
    ]
