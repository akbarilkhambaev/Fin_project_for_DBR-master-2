# Generated by Django 5.1.1 on 2025-06-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin_app_v2', '0007_alter_crmjob_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='crmtask',
            name='assigned_to',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='crmtask',
            name='subtasks',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name='crmtask',
            name='task_type',
            field=models.CharField(choices=[('SIMPLE', 'Обычная'), ('FEEDBACK', 'Обратная связь'), ('MEETING', 'Встреча')], default='SIMPLE', max_length=20),
        ),
    ]
