# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_snippet', '0002_auto_20160613_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='formatted_code',
            field=models.TextField(default='asdf'),
            preserve_default=False,
        ),
    ]
