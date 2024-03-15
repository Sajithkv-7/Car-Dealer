# Generated by Django 5.0.1 on 2024-01-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(blank=True, max_length=50, null=True)),
                ('LastName', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.EmailField(blank=True, max_length=50, null=True)),
                ('Username', models.CharField(blank=True, max_length=50, null=True)),
                ('Password', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
