# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-24 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_auto_20171224_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista_deseos',
            name='idCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente'),
        ),
    ]
