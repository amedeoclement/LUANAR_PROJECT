# Generated by Django 5.0.1 on 2024-03-06 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('luanarapp', '0004_programnature_program_campus_code_program_prospects_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='level',
        ),
    ]