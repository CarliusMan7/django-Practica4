# Generated by Django 4.2.20 on 2025-03-14 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primerapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='loan_return',
            new_name='return_date',
        ),
    ]
