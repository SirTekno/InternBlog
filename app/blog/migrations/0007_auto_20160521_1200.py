# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_snipped'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='snipped',
            new_name='snippet',
        ),
    ]
