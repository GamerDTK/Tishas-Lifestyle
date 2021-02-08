# Generated by Django 3.1.2 on 2021-01-30 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_delete_feedpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_title', models.CharField(max_length=200, unique=True)),
                ('feed_slug', models.CharField(max_length=200, unique=True)),
                ('feed_updated_on', models.DateTimeField(auto_now_add=True)),
                ('feed_content', models.TextField()),
                ('feed_created_on', models.DateTimeField(auto_now_add=True)),
                ('feed_status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('feed_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_feeds', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
