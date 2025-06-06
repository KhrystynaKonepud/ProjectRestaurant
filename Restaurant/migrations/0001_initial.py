# Generated by Django 5.2.1 on 2025-05-15 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('sort', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'category',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('guests_number', models.PositiveIntegerField()),
                ('reservation_date', models.DateField()),
                ('reservation_time', models.TimeField()),
                ('details', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Beverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_visible', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_alcoholic', models.BooleanField(default=False)),
                ('ingredients', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='beverages/')),
                ('sort', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.category')),
            ],
            options={
                'db_table': 'beverage',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_visible', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ingredients', models.TextField()),
                ('photo', models.ImageField(upload_to='dishes/')),
                ('sort', models.PositiveIntegerField(default=0)),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('is_spicy', models.BooleanField(default=False)),
                ('cuisine_type', models.CharField(default='Азіатська', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.category')),
            ],
            options={
                'db_table': 'dish',
                'ordering': ['sort'],
            },
        ),
    ]
