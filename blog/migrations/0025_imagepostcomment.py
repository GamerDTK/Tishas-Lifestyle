# Generated by Django 3.1.2 on 2021-02-01 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20210201_0754'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('video_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_post_comment', to='blog.videopost')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]