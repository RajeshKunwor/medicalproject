# Generated by Django 2.0.1 on 2019-02-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('BP', models.CharField(max_length=10)),
                ('temperature', models.FloatField(blank=True)),
                ('sugar', models.IntegerField(blank=True)),
                ('comment', models.TextField(max_length=300)),
                ('create_date', models.DateField()),
            ],
        ),
    ]
