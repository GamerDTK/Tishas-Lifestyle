# Generated by Django 3.1.2 on 2021-01-30 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210130_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='feed_doc',
        ),
    ]
