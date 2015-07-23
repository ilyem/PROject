# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 8, 18, 42, 35956, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
