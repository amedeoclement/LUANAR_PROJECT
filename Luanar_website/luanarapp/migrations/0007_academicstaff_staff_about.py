# Generated by Django 5.0.1 on 2024-04-03 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luanarapp', '0006_delete_prospectus_remove_announcement_advert_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicstaff',
            name='staff_about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
