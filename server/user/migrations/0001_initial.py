# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('uuid', models.CharField(blank=True, max_length=42, null=True)),
                ('uuid_expiration', models.DateTimeField(blank=True, null=True)),
                ('mail_registration', models.BooleanField(db_index=True, verbose_name="Receive registration's emails", help_text='To receive a mail at each new registration.(for staff members only)', default=False)),
                ('email', models.EmailField(unique=True, max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
