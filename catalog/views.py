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
    if request.method == 'GET':
        return render(request, 'home.html')
    # list all the companies
    # companies = Company.objects.all()
    # return render(
    #               request,
    #               'home.html',
    #               context={'companies' : companies,
    #                        'selected_company' : None,
    #                        'products' : None
    #                       },
    #               )


# displaying companies alphabetically.
def companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_list = [i.serialize for i in companies]
        return HttpResponse(json.dumps(companies_list))
    else:
        return HttpResponse('<h1>You are not allowed to do this operation!!</h1>')


# displaying products related to a Company
def products(request):
    """
    """
    if request.method == 'GET':
        top_products = Stock.getTop20()
        products_list = [i.serialize for i in top_products]
        return HttpResponse(json.dumps(products_list))
    else:
        return HttpResponse('<h1>You are not allowed to do this operation!!</h1>')


# to search the companies based on user's search keyword
def company_search(request, comp_search_word):
    if request.method == 'GET':
        companies = Company.objects.filter(Company_name__icontains = comp_search_word).all()
        companies_list = [i.serialize for i in companies]
        return HttpResponse(json.dumps(companies_list))
    else:
        return HttpResponse('<h1>You are not allowed to do this operation!!</h1>')


# to search the products based on user's search keyword
def product_search(request, prod_search_word):
    if request.method == 'GET':
        stocks = Stock.objects.filter(Code__in=Product.objects.filter(Product_name__icontains = prod_search_word).all()).all()
        # this is actually stocks but i have used product variable name since I display product name there predominantly
        products_list = [i.serialize for i in stocks]
        return HttpResponse(json.dumps(products_list))
    else:
        return HttpResponse('<h1>You are not allowed to do this operation!!</h1>')



# Signup page
def signup(request):
    if request.method == 'GET':
        return render(
                      request,
                      'signup.html'
                      )
    else:
        pass