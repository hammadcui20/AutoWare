# Generated by Django 4.0.1 on 2024-03-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]