# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20171227_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificacion',
            name='permisos',
        ),
        migrations.RemoveField(
            model_name='notificacion',
            name='tiempo',
        ),
        migrations.RemoveField(
            model_name='notificacion',
            name='user_destino',
        ),
    ]