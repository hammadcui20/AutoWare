# Generated by Django 4.0.1 on 2024-03-02 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_notification_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='wareteams',
            name='manager_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.manager'),
        ),
    ]