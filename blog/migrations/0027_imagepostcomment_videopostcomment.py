# Generated by Django 3.1.2 on 2021-02-01 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_delete_imagepostcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_post_comment_name', models.EmailField(max_length=254)),
                ('video_post_comment_body', models.TextField()),
                ('video_post_comment_created_on', models.DateTimeField(auto_now_add=True)),
                ('video_post_comment_active', models.BooleanField(default=False)),
                ('video_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_post_comments', to='blog.videopost')),
            ],
            options={
                'ordering': ['video_post_comment_created_on'],
            },
        ),
        migrations.CreateModel(
            name='ImagePostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_post_comment_name', models.EmailField(max_length=254)),
                ('image_post_comment_body', models.TextField()),
                ('image_post_comment_created_on', models.DateTimeField(auto_now_add=True)),
                ('image_post_comment_active', models.BooleanField(default=False)),
                ('image_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_post_comments', to='blog.imagepost')),
            ],
            options={
                'ordering': ['image_post_comment_created_on'],
            },
        ),
    ]
