window.onload = function() {
  initLoad();
};

// urls for each json endpoints
// TO-DO change all these variables on hosting
var getAllCompanies = "http://127.0.0.1:8000/catalog/companies/";
var getAllProducts = "http://127.0.0.1:8000/catalog/products/";
var getFilteredCompanies = "http://127.0.0.1:8000/catalog/companies/";
var getFilteredProducts = "http://127.0.0.1:8000/catalog/products/";
var company_products = "http://127.0.0.1:8000/catalog/company/"
var companies_div = $('#compList');
var products_div = $('#prodList');
var orders_div = $('#orderList');


// function to load the companies
function initLoad(){
    // ajax request to get all the companies
    $.getJSON(getAllCompanies, function(result){
        renderCompanies(result);
    }).fail(function(){
        console.log('failed');
    });

    // ajax request to get top20 the products
    $.getJSON(getAllProducts, function(data){
        renderProducts(data);
    }).fail(function(){
        console.log('failed');
    });
}

// function to render the company json in the first column
function renderCompanies(result){
    companies_div.empty();
    companies_list = '';
    for(i=0;i<result.length;i++){
        companies_list = '<button id="' + result[i].id+ '"type="button" class="list-group-item list-group-item-action">'+ result[i].Name + '</button>';
        companies_div.append(companies_list);
        $('#' + result[i].id).click(display_company_products);
    }
}


// function to render the products json in the middle column
function renderProducts(data){
    products_div.empty();
    products_list = '';
    for(i=0;i<data.length;i++){
        products_list = '<li id="' + data[i].code + '" class="list-group-item justify-content-between">' + data[i].Name + '<span class="badge badge-default badge-pill">' + data[i].Available + '</span></li>';
        products_div.append(products_list);
        $('#' + data[i].code).click(add_products_to_cart);
    }
}


function displayFilteredCompanies(){
    // ajax request to get the filtered companies
    // build the url with search string
    console.log($('#comp_search_word').val());
    comp_search_word = $('#comp_search_word').val();
    if(comp_search_word != ''){
        company_search_url = getFilteredCompanies + comp_search_word + '/' ;
        $.getJSON(company_search_url, function(result){
            renderCompanies(result);
        }).fail(function(){
            console.log('failed');
        });    
    }
    else{
        $.getJSON(getAllCompanies, function(result){
        renderCompanies(result);
        }).fail(function(){
            console.log('failed');
        });
    }
}

function displayFilteredProducts(){
    // ajax request to get the filtered products
    // build the url with the search string
    prod_search_word = $('#prod_search_word').val();
    if(prod_search_word != ''){
        product_search_url = getFilteredProducts + prod_search_word + '/'
        $.getJSON(product_search_url, function(data){
            renderProducts(data);
        }).fail(function(){
            console.log('failed');
        });    
    }
    else{
        $.getJSON(getAllProducts, function(data){
        renderProducts(data);
    }).fail(function(){
        console.log('failed');
    });
    }
}


// click function for the companies search
$('#search_companies').click(displayFilteredCompanies);
// click function for the products search
$('#search_products').click(displayFilteredProducts);
$('#compList > .list-group-item').on("click", function(){alert('hi');});


// function to get and display the filtered products based on the company selected.
function display_company_products(){
    // company_products += company_id + '/' ;
    productsOfComapany = '';
    productsOfComapany = company_products + this.id + '/' ;
    $.getJSON(productsOfComapany, function(data){
        renderProducts(data);
    }).fail(function(){
        console.log('failed');
    });
}


// function to add the clicked products to orders list
function add_products_to_cart(){
    console.log(this)
    console.log($(this).text());
    var product = '<li id="' + this.id + '" class="list-group-item justify-content-between">' + $(this).text() + '</span></li>';
    orders_div.append(product);
}