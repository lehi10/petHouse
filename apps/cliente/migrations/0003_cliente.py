# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 05:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registro', '0001_initial'),
        ('cliente', '0002_delete_persona'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.Persona')),
            ],
        ),
    ]
