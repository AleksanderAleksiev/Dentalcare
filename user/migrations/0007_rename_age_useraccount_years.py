# Generated by Django 4.2.5 on 2024-01-31 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_useraccount_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='age',
            new_name='years',
        ),
    ]