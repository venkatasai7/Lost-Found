# Generated by Django 4.2.7 on 2023-12-14 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_tasks_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='DueDate',
            new_name='Pickup',
        ),
    ]
