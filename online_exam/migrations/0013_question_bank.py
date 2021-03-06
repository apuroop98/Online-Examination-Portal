# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-16 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('online_exam', '0012_question_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='question_bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null='True')),
                ('description', models.TextField(blank=True, null='True')),
                ('score', models.FloatField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_exam.exam_details')),
                ('level_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_exam.level')),
                ('question_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_exam.question_type')),
                ('subtopic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_exam.subtopic')),
            ],
        ),
    ]
