# Generated by Django 2.0.1 on 2019-02-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='citizenship_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Citizenship Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ethical_group',
            field=models.CharField(blank=True, choices=[('Dalit', 'Dalit'), ('Janjati', 'Janjati'), ('Madeshi', 'Madeshi'), ('Muslin', 'Muslin'), ('Bhraman/Chetri', 'Bhraman/Chetri'), ('Ohter', 'Other')], max_length=50, null=True, verbose_name='Ethical Group'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='middle_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_no',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Phone No.'),
        ),
    ]
