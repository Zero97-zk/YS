# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-10 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20200329_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daytodo',
            name='day',
            field=models.IntegerField(default=101, verbose_name='日'),
        ),
        migrations.AlterField(
            model_name='monthtodo',
            name='month',
            field=models.IntegerField(default=4, verbose_name='月'),
        ),
        migrations.AlterField(
            model_name='weektodo',
            name='week',
            field=models.IntegerField(default=15, verbose_name='周'),
        ),
    ]
