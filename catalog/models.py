# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# to populate primary keys
import uuid

# to get the get_absolute_url
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Customer(models.Model):
    """
    This contains the model to store the users details.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    Active = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        """
        String to display the name of the firm.
        """
        return self.Name_of_the_firm


class Company(models.Model):
    """
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique identifier for company.")
    Company_name = models.CharField(max_length=250, help_text="Enter the company name.")

    def __str__(self):
        """
        """
        return self.Company_name

    def get_absolute_url(self):
        """
        """
        return reverse('company_products', args=[str(self.id)])

    # static method to return json list of companies
    @property
    def serialize(self):
        return {
        "id" : str(self.id) ,
        "Name" : str(self.Company_name)
        }


class Product(models.Model):
    """
    This contains the details of the products.
    """
    Code = models.IntegerField(primary_key=True, help_text="Enter the code for the product.")
    Product_name = models.CharField(max_length=250, null=False, help_text="Enter the product name.")
    Company = models.ForeignKey('Company', on_delete=models.CASCADE, null=False)

    def __str__(self):
        """
        """
        return str(self.Code)

    @property
    def serialize(self):
        return {
        "id" : str(self.id) ,
        "Name" : str(self.Company_name)
        }


class Stock(models.Model):
    """
    """
    Code = models.ForeignKey('Product', on_delete=models.CASCADE)
    Available_units = models.IntegerField(help_text="Enter the number of available units.")

    def __str__(self):
        """
        """
        return str(self.Code)

    # top 20 products on stock availability to display initially
    @staticmethod
    def getTop20():
        return Stock.objects.order_by('-Available_units')[:20]

    @classmethod
    def getCompanyProducts(company_id):
        pass


    @property
    def serialize(self):
        return {
        "code" : str(self.Code) ,
        "Name" : str(self.Code.Product_name),
        "Available" : str(self.Available_units)
        }


class Order(models.Model):
    """
    """
    OrderId = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique identifier to identify orders.")
    Order_date = models.DateTimeField(auto_now=True)
    Placed_by = models.ForeignKey(settings.AUTH_USER_MODEL)


    def __str__(self):
        """
        """
        return self.OrderId
    @property
    def serialize(self):
        return {
        "id" : str(self.id) ,
        "Name" : str(self.Company_name)
        }

class OrderDetails(models.Model):
    """
    """
    Row_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique key to identify an order details.")
    OrderId = models.ForeignKey('Order')
    Code = models.ForeignKey('Product')
    Quantity = models.IntegerField(help_text="Enter the required quantity.")

    @property
    def serialize(self):
        return {
        "id" : str(self.id) ,
        "Name" : str(self.Company_name)
        }