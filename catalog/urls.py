from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^company/(?P<uuid>[^/]+)/$', views.products, name='company_products'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^companies/$', views.companies, name='compList'),
    url(r'^products/$', views.products, name='prodList'),
    url(r'^companies/(?P<comp_search_word>[a-zA-Z0-9]*)/$', views.company_search, name='company_search'),
    url(r'^products/(?P<prod_search_word>[a-zA-Z0-9]*)/$', views.product_search, name='product_search'),
]