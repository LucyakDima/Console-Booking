# Generated by Django 5.2 on 2025-05-07 11:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gaming_rooms_count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GamingConsole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('generation', models.IntegerField()),
                ('controllers_count', models.IntegerField(default=1)),
                ('price_per_hour', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'Gaming Console',
                'verbose_name_plural': 'Gaming Consoles',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ConsoleBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('gaming_console', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.gamingconsole')),
            ],
            options={
                'verbose_name': 'Console Booking',
                'verbose_name_plural': 'Console Bookings',
                'ordering': ['start_time'],
            },
        ),
        migrations.CreateModel(
            name='GamingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('capacity', models.IntegerField(default=1)),
                ('price_per_hour', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.city')),
                ('consoles', models.ManyToManyField(related_name='rooms', to='booking.gamingconsole')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='RoomBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gaming_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.gamingroom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Room Booking',
                'verbose_name_plural': 'Room Bookings',
                'ordering': ['start_time'],
            },
        ),
    ]
