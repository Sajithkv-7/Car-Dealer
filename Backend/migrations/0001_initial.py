# Generated by Django 5.0.1 on 2024-01-15 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Model', models.CharField(blank=True, max_length=50, null=True)),
                ('Description', models.CharField(blank=True, max_length=200, null=True)),
                ('Image_1', models.ImageField(blank=True, null=True, upload_to='Car-Images')),
                ('Image_2', models.ImageField(blank=True, null=True, upload_to='Car-Images')),
                ('Image_3', models.ImageField(blank=True, null=True, upload_to='Car-Images')),
                ('Image_4', models.ImageField(blank=True, null=True, upload_to='Car-Images')),
                ('Body_Style', models.CharField(blank=True, max_length=50, null=True)),
                ('Features', models.CharField(blank=True, max_length=200, null=True)),
                ('Price', models.CharField(blank=True, max_length=50, null=True)),
                ('Mileage', models.CharField(blank=True, max_length=50, null=True)),
                ('Engine', models.CharField(blank=True, max_length=50, null=True)),
                ('Transmission', models.CharField(blank=True, max_length=50, null=True)),
                ('Fuel_Type', models.CharField(blank=True, max_length=50, null=True)),
                ('Seats', models.IntegerField(blank=True, null=True)),
                ('Color', models.CharField(blank=True, max_length=50, null=True)),
                ('Doors', models.IntegerField(blank=True, null=True)),
                ('Year', models.IntegerField(blank=True, null=True)),
                ('Type', models.CharField(blank=True, max_length=50, null=True)),
                ('Power', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
