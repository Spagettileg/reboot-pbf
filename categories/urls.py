from django.conf.urls import url, include
from .views import product_filter

# Product filter to include view all, junior and adult rugby boot products.
urlpatterns = [
url(r'(?P<category>\w+)/$', product_filter, name='product-filter'),
]