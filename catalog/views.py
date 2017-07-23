# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# import all the database objects
from .models import User, Company, Product, Stock, Order, OrderDetails


# Signup page for users.
def index(request):
    """
    """
    # list all the companies
    companies = Company.objects.all()
    return render(
                  request,
                  'home.html',
                  context={'companies' : companies,
                           'selected_company' : None,
                           'products' : None
                          },
                  )


# displaying products related to a Company
def products(request, uuid):
    """
    """
    # list all prodcts of a Company
    companies = Company.objects.all()
    selected_company = Company.objects.filter(id=uuid).first()
    products = Product.objects.filter(Company=selected_company).all()
    products_stock = {}
    # for product in products:
    #     products_stock[product] = Stock.objects.filter(Code=product, available_units > 0).first().available_units
    # print products_stock
    return render(
                  request,
                  'home.html',
                  context={'companies' : companies,
                           'selected_company' : selected_company,
                           'products' : products
                          },
                  )
