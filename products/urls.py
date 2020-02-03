from django.conf.urls import url, include
from products import views as product_views

urlpatterns = [
    url(r'^$', product_views.all_products, name='products'),
    url(r'^$', product_views.categories, name='categories'),
    url(r'^$', product_views.show_all_purchases, name="show_all_purchases"),
    url(r'^(?P<pk>\d+)/$', product_views.product_detail, name='product-detail'),
]