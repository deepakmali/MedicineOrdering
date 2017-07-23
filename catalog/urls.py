from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^company/(?P<uuid>[^/]+)/$', views.products, name='company_products'),
]