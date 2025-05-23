# Generated by Django 5.2 on 2025-04-15 06:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_brand_new', models.BooleanField(default=True)),
                ('quality_description', models.TextField(blank=True)),
                ('seller_whatsapp', models.CharField(max_length=15)),
                ('seller_instagram', models.CharField(blank=True, max_length=50)),
                ('seller_phone', models.CharField(blank=True, max_length=15)),
                ('seller_email', models.EmailField(blank=True, max_length=254)),
                ('delivery_cost', models.CharField(max_length=50)),
                ('delivery_location', models.CharField(max_length=100)),
                ('delivery_method', models.CharField(max_length=100)),
                ('seller_location', models.CharField(max_length=100)),
                ('is_negotiable', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_available', models.BooleanField(default=True)),
                ('is_weekly_offer', models.BooleanField(default=False)),
                ('is_new_arrival', models.BooleanField(default=False)),
            ],
        ),
    ]
