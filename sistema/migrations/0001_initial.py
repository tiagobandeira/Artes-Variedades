# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-08 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('preco', models.FloatField()),
                ('data_publicacao', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]