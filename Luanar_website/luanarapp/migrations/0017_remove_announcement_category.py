# Generated by Django 5.0.6 on 2024-06-15 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('luanarapp', '0016_announcement_tag_event_tag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='category',
        ),
    ]
