# Generated by Django 3.1.4 on 2020-12-19 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pmanage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tasks',
            new_name='complete_percentage',
        ),
        migrations.AddField(
            model_name='project',
            name='task',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=64)),
                ('percentage', models.IntegerField()),
                ('projectid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pmanage.project')),
            ],
        ),
    ]