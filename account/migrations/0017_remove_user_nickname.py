# Generated by Django 3.2.9 on 2024-01-02 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20240102_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
    ]