# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 05:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links_everywhere', '0003_auto_20160313_0406'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='URLMetaData',
            new_name='Usermetadata',
        ),
        migrations.RenameField(
            model_name='usermetadata',
            old_name='img_link',
            new_name='img',
        ),
    ]
