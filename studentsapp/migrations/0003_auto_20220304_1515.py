# Generated by Django 3.2.6 on 2022-03-04 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsapp', '0002_rename_idd_subjectmodel_stu_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjectmodel',
            old_name='arabic',
            new_name='mark',
        ),
        migrations.RemoveField(
            model_name='subjectmodel',
            name='biology',
        ),
        migrations.RemoveField(
            model_name='subjectmodel',
            name='chemistry',
        ),
        migrations.RemoveField(
            model_name='subjectmodel',
            name='english',
        ),
        migrations.RemoveField(
            model_name='subjectmodel',
            name='maths',
        ),
        migrations.RemoveField(
            model_name='subjectmodel',
            name='physics',
        ),
        migrations.AddField(
            model_name='subjectmodel',
            name='subject',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
