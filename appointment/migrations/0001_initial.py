# Generated by Django 2.0.1 on 2019-03-11 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=10)),
                ('appointment_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_schedule', to='doctor.DoctorSchedule')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_d', to='doctor.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_p', to='patient.Patient')),
            ],
        ),
    ]
