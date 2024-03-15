# Generated by Django 5.0.1 on 2024-01-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.EmailField(blank=True, max_length=50, null=True)),
                ('Subject', models.CharField(blank=True, max_length=50, null=True)),
                ('Message', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
