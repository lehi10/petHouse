# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 07:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0002_auto_20171127_0748'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='Proveedor',
        ),
    ]
