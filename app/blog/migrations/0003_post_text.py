# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('blog', '0002_auto_20160520_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=cms.models.fields.PlaceholderField(to='cms.Placeholder', null=True, editable=False, slotname='blog_text'),
        ),
    ]
