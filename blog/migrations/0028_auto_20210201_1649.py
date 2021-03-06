# Generated by Django 3.1.2 on 2021-02-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_imagepostcomment_videopostcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagepostcomment',
            name='image_post_comment_email',
            field=models.EmailField(default='dekeji1@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='videopostcomment',
            name='video_post_comment_email',
            field=models.EmailField(default='dekeji1@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='imagepostcomment',
            name='image_post_comment_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='videopostcomment',
            name='video_post_comment_name',
            field=models.CharField(max_length=200),
        ),
    ]
