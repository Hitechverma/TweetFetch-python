# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20150411_2056'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tweets',
            new_name='Haircut',
        ),
    ]
