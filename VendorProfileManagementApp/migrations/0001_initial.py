# Generated by Django 4.2.7 on 2023-12-11 18:15

import VendorProfileManagementApp.models
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VendorModel',
            fields=[
                ('vendor_code', models.CharField(default=uuid.uuid4, editable=False, max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('contact_details', models.TextField()),
                ('address', models.TextField()),
                ('on_time_delivery_rate', models.FloatField(null=True)),
                ('quality_rating_avg', models.FloatField(null=True)),
                ('average_response_time', models.FloatField(null=True)),
                ('fulfillment_rate', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderModel',
            fields=[
                ('po_number', models.CharField(default=VendorProfileManagementApp.models.generate_unique_number, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('quality_rating', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(10.0)])),
                ('delivery_date', models.DateField()),
                ('delivery_status', models.CharField(choices=[('Y', 'On Time'), ('N', 'Delayed')], max_length=1, null=True)),
                ('issue_date', models.DateTimeField(default=datetime.datetime(2023, 12, 11, 23, 45, 48, 246248))),
                ('acknowledgment_date', models.DateTimeField(null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VendorProfileManagementApp.vendormodel')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalPerformanceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('on_time_delivery_rate', models.FloatField(null=True)),
                ('quality_rating_avg', models.FloatField(null=True)),
                ('average_response_time', models.FloatField(null=True)),
                ('fulfillment_rate', models.FloatField(null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VendorProfileManagementApp.vendormodel')),
            ],
        ),
    ]