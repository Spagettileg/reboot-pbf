from django.conf.urls import url, include
from .views import index, contact

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^contact/$', contact, name='contact'),
]