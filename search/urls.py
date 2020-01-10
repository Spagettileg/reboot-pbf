from django.conf.urls import url
from .views import run_search

urlpatterns = [
    url(r'^$', run_search, name='search')
]