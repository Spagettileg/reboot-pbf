from django.conf.urls import url, include
from .views import all_products, product_detail, categories

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^$', categories, name='categories'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product-detail'),
]
