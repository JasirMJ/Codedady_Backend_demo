# Generated by Django 4.0.3 on 2022-03-09 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentwithrelation', '0004_studentclass'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentClass',
        ),
    ]
