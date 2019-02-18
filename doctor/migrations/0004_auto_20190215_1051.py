# Generated by Django 2.0.1 on 2019-02-15 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20190212_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=10)),
                ('shift', models.CharField(choices=[('Morining', 'Morining'), ('Evening', 'Evening'), ('Day', 'Day')], max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='citizenship_number',
            field=models.CharField(blank=True, default='', max_length=50, unique=True, verbose_name='Citizenship Number'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone_no',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='Phone No.'),
        ),
        migrations.AddField(
            model_name='doctorschedule',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_schedule', to='doctor.Doctor'),
        ),
    ]
