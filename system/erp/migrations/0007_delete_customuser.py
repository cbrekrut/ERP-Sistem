# Generated by Django 5.0.1 on 2024-03-03 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_alter_task_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]