# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0024_auto_20171224_0725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requerimientos',
            fields=[
                ('idRequerimiento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=300)),
                ('cantidad', models.IntegerField(default=0)),
            ],
        ),
    ]
