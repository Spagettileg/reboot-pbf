from django.conf.urls import url, include
from .views import (index, contact, explained, faqs, juniors, adults,
                    bootquality, cookie, privacy)

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^contact/$', contact, name='contact'),
    url(r'^explained/$', explained, name='explained'),
    url(r'^faqs/$', faqs, name='faqs'),
    url(r'^juniors/$', juniors, name='juniors'),
    url(r'^adults/$', adults, name='adults'),
    url(r'^bootquality/$', bootquality, name='bootquality'),
    url(r'^cookie/$', cookie, name='cookie'),
    url(r'^privacy/$', privacy, name='privacy'),
]