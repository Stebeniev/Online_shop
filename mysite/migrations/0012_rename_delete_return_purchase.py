# Generated by Django 4.1.6 on 2023-02-21 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_alter_myuser_wallet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='return',
            old_name='delete',
            new_name='purchase',
        ),
    ]
