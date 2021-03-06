# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 07:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0002_user_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_the_firm', models.CharField(help_text='Enter the name of your firm.', max_length=100)),
                ('Address', models.TextField(help_text='Enter the Delivery address.', max_length=500)),
                ('Pincode', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Contact_person', models.CharField(help_text='Enter the Name of the contact person.', max_length=50)),
                ('Designation', models.CharField(help_text='Enter the designation of the contact person.', max_length=50)),
                ('Office_phone', models.CharField(help_text='Enter office phone number.', max_length=15)),
                ('Mobile_phone', models.CharField(help_text='Enter mobile number.', max_length=13)),
                ('Drug_License', models.CharField(help_text='Enter the Valid Drug License Number.', max_length=100)),
                ('DL_expiry_date', models.DateField(help_text='Enter the Drug license Expiry date.')),
                ('GSTIN', models.CharField(help_text='Enter the GSTIN number.', max_length=50)),
                ('Active', models.BooleanField(default=True)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='Placed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Customer'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
