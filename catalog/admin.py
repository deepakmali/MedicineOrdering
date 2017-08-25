# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from  .models import Customer, Company, Product, Stock, Order, OrderDetails

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Company)