# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hustle_science_pkg', '0002_auto_20150609_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_type', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='post',
            name='video_iframe',
        ),
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='media_iframe',
            field=embed_video.fields.EmbedVideoField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='screenshot',
            field=models.ImageField(null=True, upload_to=b'app_screenshots', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=b'', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='project_iframe',
            field=models.URLField(null=True, blank=True),
        ),
    ]
