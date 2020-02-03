from django.conf.urls import url, include
from products import views as product_views

urlpatterns = [
    url(r'^$', product_views.all_products, name='products'),
    url(r'^$', product_views.categories, name='categories'),
    url(r'^(?P<id>\d+)/$', product_views.product_detail, name='product-detail'),
    url(r'^create_product/$', product_views.create_a_product, name='create_a_product'),
]