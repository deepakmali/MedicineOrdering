# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# to populate primary keys
import uuid

# Create your models here.
class User(models.Model):
    """
    This contains the model to store the users details.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique identification for user.")
    Name_of_the_firm = models.CharField(max_length=100, help_text="Enter the name of your firm.")
    Address = models.TextField(max_length=500, help_text="Enter the Delivery address.")
    Pincode = models.IntegerField()
    Email = models.EmailField()
    Contact_person = models.CharField(max_length=50, null=False, help_text="Enter the Name of the contact person.")
    Designation = models.CharField(max_length=50, help_text="Enter the designation of the contact person.")
    Office_phone = models.CharField(max_length=15, help_text="Enter office phone number.")
    Mobile_phone = models.CharField(max_length=13, null=False, help_text="Enter mobile number.")
    Drug_License = models.CharField(max_length=100, null=False, help_text="Enter the Valid Drug License Number.")
    DL_expiry_date = models.DateField(help_text="Enter the Drug license Expiry date.")
    GSTIN = models.CharField(max_length=50, null=False, help_text="Enter the GSTIN number.")
    Active = models.BooleanField(default=False)

    def __str__(self):
        """
        String to display the name of the firm.
        """
        return self.Name_of_the_firm


class Product(models.Model):
    """
    This contains the details of the products.
    """
    Code = models.IntegerField(primary_key=True, help_text="Enter the code for the product.")
    Product_name = models.CharField(max_length=250, null=False, help_text="Enter the product name.")
    Company = models.CharField(max_length=250, null=False, help_text="Enter the company name.")

    def __str__(self):
        """
        """
        return self.Product_name


class Stock(models.Model):
    """
    """
    Code = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    Available_units = models.IntegerField(help_text="Enter the number of available units.")

    def __str__(self):
        """
        """
        return self.Code


class Order(models.Model):
    """
    """
    OrderId = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique identifier to identify orders.")
    Order_date = models.DateTimeField(auto_now=True)
    Placed_by = models.ForeignKey('User')


    def __str__(self):
        """
        """
        return self.OrderId


class OrderDetails(models.Model):
    """
    """
    Row_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique key to identify an order details.")
    OrderId = models.ForeignKey('Order')
    Code = models.ForeignKey('Product')
    Quantity = models.IntegerField(help_text="Enter the required quantity.")