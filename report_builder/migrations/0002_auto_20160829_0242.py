# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 02:42
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('async_notifications', '0002_auto_20160515_0018'),
        ('report_builder', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReviewerTree',
            new_name='RevisionTree',
        ),
        migrations.RenameModel(
            old_name='TreeReviewer',
            new_name='RevisionTreeUser',
        ),
        migrations.DeleteModel(
            name='EmailNotificationQueue',
        ),
        migrations.RemoveField(
            model_name='questioninforelation',
            name='parent_question',
        ),
        migrations.RemoveField(
            model_name='questioninforelation',
            name='question',
        ),
        migrations.RemoveField(
            model_name='questioninforelation',
            name='report',
        ),
        migrations.AlterModelOptions(
            name='revisiontree',
            options={'verbose_name': 'Revision Tree', 'verbose_name_plural': 'Revision Tree'},
        ),
        migrations.AlterModelOptions(
            name='revisiontreeuser',
            options={'verbose_name': 'Revision Tree User', 'verbose_name_plural': 'Revision Tree Users'},
        ),
        migrations.RenameField(
            model_name='revisiontree',
            old_name='tree_reviewer',
            new_name='revision_tree_user',
        ),
        migrations.RemoveField(
            model_name='reporttype',
            name='responsable_change_notification',
        ),
        migrations.RemoveField(
            model_name='reporttype',
            name='subject_action_ok',
        ),
        migrations.RemoveField(
            model_name='reporttype',
            name='subject_report_start',
        ),
        migrations.RemoveField(
            model_name='reporttype',
            name='subject_revision_turn',
        ),
        migrations.AddField(
            model_name='reporttype',
            name='report_end',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='report_end', to='async_notifications.EmailTemplate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reporttype',
            name='responsable_change',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='responsable_change', to='async_notifications.EmailTemplate'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_options',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='questions',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='report',
            name='template',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=[{'human_name': 'General information', 'name': 'categ0', 'order': 0, 'subcategories': [{'human_name': 'General information', 'name': 'categ0_categ0', 'order': 0, 'question': [], 'questions': []}], 'subcategories_count': 1}]),
        ),
        migrations.AlterField(
            model_name='reporttype',
            name='action_ok',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_ok', to='async_notifications.EmailTemplate'),
        ),
        migrations.AlterField(
            model_name='reporttype',
            name='report_start',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_start', to='async_notifications.EmailTemplate'),
        ),
        migrations.AlterField(
            model_name='reporttype',
            name='revision_turn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revision_turn', to='async_notifications.EmailTemplate'),
        ),
        migrations.DeleteModel(
            name='QuestionInfoRelation',
        ),
    ]
