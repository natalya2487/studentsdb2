# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-14 09:43
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_auto_20170814_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='student',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='group', chained_model_field='student_group', on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
        ),
    ]