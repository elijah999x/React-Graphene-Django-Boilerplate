# Generated by Django 3.2.10 on 2023-04-08 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='todo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action', to='todo.todo'),
        ),
    ]