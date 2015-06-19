# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hustle_science_pkg', '0004_auto_20150612_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='post',
            name='content_type',
            field=models.ForeignKey(default='', to='hustle_science_pkg.Content_Type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='short_desc',
            field=models.CharField(default=b'', max_length=144),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
