# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 08:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0004_auto_20170812_1533'),
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
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='order',
            name='Placed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]