from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new_post/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit_post/$', create_or_edit_post, name='edit_post'),
    ]
