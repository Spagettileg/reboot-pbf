from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    url('^$', PasswordResetView,
        {'post_reset_redirect': reverse_lazy('PasswordResetDoneView')},
        name='PasswordResetView'),
    url(r'^done/$', PasswordResetDoneView, name='PasswordResetDoneView'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView,
        {'post_reset_redirect': reverse_lazy('PasswordResetCompleteView')},
        name='PasswordResetConfirmView'),
    url(r'^complete/$', PasswordResetCompleteView, name='PasswordResetCompleteView'),
]