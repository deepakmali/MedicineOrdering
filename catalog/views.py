# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# for testing http response, remove this later
from django.http import HttpResponse
import simplejson as json 

# Create your views here.
# import all the database objects
from .models import Customer, Company, Product, Stock, Order, OrderDetails

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


# displaying top 20 available products.
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


# to search products based on companies
def company_products(request, uuid):
    if request.method == 'GET':
        stocks = Stock.objects.filter(Code__in = Product.objects.filter(Company = uuid).all()).all()
        products_list = [i.serialize for i in stocks]
        return HttpResponse(json.dumps(products_list))
    else:
        return HttpResponse('<h1>You are not allowed to do this operation!!</h1>')


# Signup page
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # print form.cleaned_data.get('Name_of_the_firm')
            print form.cleaned_data.get('Name_of_the_firm')
            print form.cleaned_data.get('Address')
            print form.cleaned_data.get('Pincode')
            print form.cleaned_data.get('Email')
            print form.cleaned_data.get('Contact_person')
            print form.cleaned_data.get('Designation')
            print form.cleaned_data.get('Office_phone')
            print form.cleaned_data.get('Mobile_phone')
            print form.cleaned_data.get('Drug_License')
            print form.cleaned_data.get('DL_expiry_date')
            print form.cleaned_data.get('GSTIN')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = User.objects.get(username=username)
            print user.username
            newCustomer = Customer(user = user,
                                   Name_of_the_firm = form.cleaned_data.get('Name_of_the_firm'),
                                   Address = form.cleaned_data.get('Address'),
                                   Pincode = form.cleaned_data.get('Pincode'),
                                   Email = form.cleaned_data.get('Email'),
                                   Contact_person = form.cleaned_data.get('Contact_person'),
                                   Designation = form.cleaned_data.get('Designation'),
                                   Office_phone = form.cleaned_data.get('Office_phone'),
                                   Mobile_phone = form.cleaned_data.get('Mobile_phone'),
                                   Drug_License = form.cleaned_data.get('Drug_License'),
                                   DL_expiry_date = form.cleaned_data.get('DL_expiry_date'),
                                   GSTIN = form.cleaned_data.get('GSTIN')
                                   )
            # newCustomer.user = user
            # newCustomer.Name_of_the_firm = form.cleaned_data.get('Name_of_the_firm')
            # newCustomer.Address = form.cleaned_data.get('Address')
            # newCustomer.Pincode = form.cleaned_data.get('Pincode')
            # newCustomer.Email = form.cleaned_data.get('Email')
            # newCustomer.Contact_person = form.cleaned_data.get('Contact_person')
            # newCustomer.Designation = form.cleaned_data.get('Designation')
            # newCustomer.Office_phone = form.cleaned_data.get('Office_phone')
            # newCustomer.Mobile_phone = form.cleaned_data.get('Mobile_phone')
            # newCustomer.Drug_License = form.cleaned_data.get('Drug_License')
            # newCustomer.DL_expiry_date = form.cleaned_data.get('DL_expiry_date')
            # newCustomer.GSTIN = form.cleaned_data.get('GSTIN')
            newCustomer.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})