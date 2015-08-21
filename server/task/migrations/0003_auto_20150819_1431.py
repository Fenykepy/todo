# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20150819_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_time',
            field=models.DateTimeField(null=True, verbose_name='Due time', db_index=True, blank=True),
        ),
    ]
