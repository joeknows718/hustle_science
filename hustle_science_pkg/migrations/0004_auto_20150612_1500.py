# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hustle_science_pkg', '0003_auto_20150612_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='project_iframe',
            new_name='project_url',
        ),
    ]
