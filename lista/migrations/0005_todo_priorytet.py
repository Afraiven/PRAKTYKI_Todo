# Generated by Django 3.1.5 on 2022-03-22 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0004_remove_todo_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priorytet',
            field=models.CharField(default='1', max_length=2),
        ),
    ]
