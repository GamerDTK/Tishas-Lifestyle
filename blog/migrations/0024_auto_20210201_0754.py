# Generated by Django 3.1.2 on 2021-01-31 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20210201_0747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='feed_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='feed_created_on',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='feed_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='feed_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='feed_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='feed_updated_on',
            new_name='updated_on',
        ),
    ]
