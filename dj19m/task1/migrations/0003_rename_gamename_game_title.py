# Generated by Django 5.1.5 on 2025-01-28 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_rename_username_buyer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='gamename',
            new_name='title',
        ),
    ]
