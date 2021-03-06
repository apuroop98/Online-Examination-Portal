# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-25 08:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_exam', '0026_auto_20181025_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='question_bank',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='topic',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='exam_detail',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_exam.course'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_exam.user'),
        ),
    ]
