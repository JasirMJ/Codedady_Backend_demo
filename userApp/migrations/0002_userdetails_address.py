# Generated by Django 4.0.3 on 2022-03-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
