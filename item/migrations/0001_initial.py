# Generated by Django 5.1.3 on 2025-03-01 14:30

import cloudinary.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usermanagament', '0004_alter_profile_referred_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item_type', models.CharField(choices=[('student', 'Student'), ('doctor', 'Doctor')], max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='item.category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('items', models.ManyToManyField(related_name='orders', to='item.item')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='usermanagament.profile')),
            ],
        ),
        migrations.CreateModel(
            name='PackageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='item.package')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PackageOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='item.package')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packageOrders', to='usermanagament.profile')),
            ],
        ),
    ]
