# Generated by Django 2.0.1 on 2019-02-12 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='expirty_date',
            new_name='expiry_date',
        ),
    ]
