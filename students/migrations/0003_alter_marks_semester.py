# Generated by Django 4.0.3 on 2022-03-04 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_marks_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='Semester',
            field=models.CharField(default='1', max_length=100),
        ),
    ]
