# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 10:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_store', '0030_store_tablename'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='suggestion',
            table='pootle_store_suggestion',
        ),
    ]
