# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-21 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0456 \u0447\u0430\u0441 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u043d\u044f'),
        ),
    ]
