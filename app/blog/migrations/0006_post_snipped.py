# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snipped',
            field=models.TextField(blank=True, null=True),
        ),
    ]
