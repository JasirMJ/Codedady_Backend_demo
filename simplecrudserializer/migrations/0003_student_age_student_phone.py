# Generated by Django 4.0.3 on 2022-03-09 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplecrudserializer', '0002_delete_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
    ]
