from django.conf.urls import url, include
from products import views as product_views

urlpatterns = [
    url(r'^$', product_views.all_products, name='products'),
    url(r'^$', product_views.categories, name='categories'),
    url(r'^$', product_views.show_all_purchases, name="show_all_purchases"),
    url(r'^(?P<pk>\d+)/$', product_views.product_detail, name='product-detail'),
    url(r'^(?P<pk>\d+)/edit_product/$', product_views.edit_a_product, name="edit_a_product"),
    url(r'^(?P<pk>\d+)/delete_product/$', product_views.delete_a_product, name="delete_a_product"),
    url(r'^(?P<pk>\d+)create_a_product/$', product_views.create_a_product, name="create_a_product"),
]