# Generated by Django 4.1.5 on 2023-01-21 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
                ('province', models.CharField(max_length=70)),
                ('postal', models.PositiveIntegerField()),
                ('birthday', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.PositiveIntegerField()),
            ],
        ),
    ]
