# Generated by Django 3.1.4 on 2020-12-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pmanage', '0003_remove_project_task_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='taskpercentage',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
