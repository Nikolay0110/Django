# Generated by Django 4.2.4 on 2023-08-09 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('room', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.IntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('che', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor')),
            ],
        ),
    ]