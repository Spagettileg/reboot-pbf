from django.conf.urls import url, include
from .views import all_products, product_detail, categories, edit_a_product, create_a_product, delete_a_product

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^$', categories, name='categories'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product-detail'),
    url(r'^(?P<pk>\d+)/edit_product/$', edit_a_product, name="edit_a_product"),
    url(r'^(?P<pk>\d+)/delete_product/$', delete_a_product, name="delete_a_product"),
    url(r'^create_product/$', create_a_product, name='create_a_product'),
]