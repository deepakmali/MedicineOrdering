# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# for testing http response, remove this later
from django.http import HttpResponse
import simplejson as json 

# Create your views here.
# import all the database objects
from .models import User, Company, Product, Stock, Order, OrderDetails

# for ajax requests
# from jsonify.decorators import ajax_request

# Signup page for users.
# @ajax_request
def index(request):
    """
    """
    # list all the companies
    companies = Company.objects.all()
    # return render(
    #               request,
    #               'home.html',
    #               context={'companies' : companies,
    #                        'selected_company' : None,
    #                        'products' : None
    #                       },
    #               )
    # return jsonify(companies_list = [i.serialize for i in companies])
    companies_list = [i.serialize for i in companies]
    # return {'companies' : companies_list}
    print companies_list
    return HttpResponse(json.dumps(companies_list))


# displaying products related to a Company
def products(request, uuid):
    """
    """
    # list all prodcts of a Company
    print request.method
    if request.method == 'GET':
        companies = Company.objects.all()
        selected_company = Company.objects.filter(id=uuid).first()
        # products = Product.objects.filter(Company=selected_company).all()
        # products_stock = {}
        stocks = Stock.objects.filter(Code__in=Product.objects.filter(Company=selected_company).all()).all()
        print stocks
        # for product in products:
        #     products_stock[product] = Stock.objects.filter(Code=product, available_units > 0).first().available_units
        # print products_stock
        return render(
                      request,
                      'home.html',
                      context={'companies' : companies,
                               'selected_company' : selected_company,
                               # 'products' : products,
                               'stocks' : stocks
                              },
                      )


# Signup page
def signup(request):
    if request.method == 'GET':
        return render(
                      request,
                      'signup.html'
                      )
    else:
        pass