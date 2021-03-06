# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-18 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0024_auto_20170916_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='teacher_en',
            field=models.CharField(max_length=256, null=True, verbose_name='\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447'),
        ),
        migrations.AddField(
            model_name='exam',
            name='teacher_uk',
            field=models.CharField(max_length=256, null=True, verbose_name='\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447'),
        ),
        migrations.AddField(
            model_name='exam',
            name='title_en',
            field=models.CharField(max_length=256, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0443'),
        ),
        migrations.AddField(
            model_name='exam',
            name='title_uk',
            field=models.CharField(max_length=256, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0443'),
        ),
    ]
