# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20160126_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='success',
        ),
    ]
