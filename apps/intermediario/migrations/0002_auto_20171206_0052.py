# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intermediario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idProveedor', models.AutoField(primary_key=True, serialize=False)),
                ('ruc', models.CharField(db_index=True, max_length=20)),
                ('razonSocial', models.CharField(db_index=True, max_length=100)),
                ('encargado', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=20, null=True)),
                ('telf', models.CharField(max_length=15, null=True)),
                ('domicilio', models.TextField(max_length=100)),
                ('email', models.CharField(max_length=50, null=True)),
                ('info', models.CharField(max_length=300)),
                ('usuario', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('calificacion', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='intermediario',
            name='persona',
        ),
        migrations.DeleteModel(
            name='Intermediario',
        ),
    ]
