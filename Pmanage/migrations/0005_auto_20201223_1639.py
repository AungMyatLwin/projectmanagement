# Generated by Django 3.1.4 on 2020-12-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pmanage', '0004_tasks_taskpercentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='taskpercentage',
            field=models.IntegerField(default=0),
        ),
    ]
