# Generated by Django 5.1.3 on 2024-11-14 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_alter_logs_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logs',
            options={'get_latest_by': 'date_created'},
        ),
    ]