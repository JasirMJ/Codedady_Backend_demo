# Generated by Django 4.0.3 on 2022-03-04 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='Semester',
            field=models.CharField(default='sem1', max_length=100),
        ),
    ]