# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('code_snippet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='language',
            new_name='lexer',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='id',
        ),
        migrations.AddField(
            model_name='snippet',
            name='cmsplugin_ptr',
            field=models.OneToOneField(serialize=False, primary_key=True, to='cms.CMSPlugin', parent_link=True, default=1, auto_created=True),
            preserve_default=False,
        ),
    ]
