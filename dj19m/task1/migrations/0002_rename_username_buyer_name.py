# Generated by Django 5.1.5 on 2025-01-28 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='username',
            new_name='name',
        ),
    ]
