# Generated by Django 5.0.1 on 2024-04-03 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('luanarapp', '0007_academicstaff_staff_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academicstaff',
            old_name='staff_about',
            new_name='about_staff',
        ),
    ]
