from django.conf.urls import url, include
from .views import ProductCreateView


urlpatterns = [
    url(r'^$', ProductCreateView, name='products'),
    ]