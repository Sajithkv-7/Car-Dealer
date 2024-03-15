# Generated by Django 5.0.1 on 2024-01-29 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0002_contactdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.EmailField(blank=True, max_length=50, null=True)),
                ('Mobile', models.CharField(blank=True, max_length=50, null=True)),
                ('Place', models.CharField(blank=True, max_length=50, null=True)),
                ('Description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]