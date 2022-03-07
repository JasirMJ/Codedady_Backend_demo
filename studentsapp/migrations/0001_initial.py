# Generated by Django 3.2.6 on 2022-03-03 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.IntegerField()),
                ('english', models.FloatField(default=0.0)),
                ('maths', models.FloatField(default=0.0)),
                ('physics', models.FloatField(default=0.0)),
                ('chemistry', models.FloatField(default=0.0)),
                ('biology', models.FloatField(default=0.0)),
                ('arabic', models.FloatField(default=0.0)),
            ],
        ),
    ]