# Generated by Django 4.1.6 on 2023-02-06 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_alter_myuser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': 'MyUser', 'verbose_name_plural': 'MyUsers'},
        ),
    ]