# Generated by Django 4.1.6 on 2023-02-05 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=60)),
                ('model', models.CharField(max_length=60)),
                ('year', models.IntegerField(blank=True)),
                ('price', models.IntegerField(blank=True)),
            ],
        ),
    ]
