from django.conf.urls import url
from .views import (show_all_feedbacks, single_feedback_view,
                    create_a_feedback, edit_a_feedback, delete_a_feedback)

urlpatterns = [
    url(r'^$', show_all_feedbacks, name="show_all_feedbacks"),
    url(r'^(?P<pk>\d+)/$', single_feedback_view, name="single_feedback_view"),
    url(r'^create_bug/$', create_a_feedback, name="create_a_feedback"),
    url(r'^(?P<pk>\d+)/edit_feedback/$', edit_a_feedback,
                                        name="edit_a_feedback"),
    url(r'^(?P<pk>\d+)/delete_feedback/$', delete_a_feedback,
                                        name="delete_a_feedback"),
    ]