# Generated by Django 4.0.3 on 2022-04-20 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='name',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relations.productsrelationmodel'),
        ),
    ]
