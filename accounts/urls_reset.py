from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    url('^$', PasswordResetView, {'post_reset_redirect': reverse_lazy('PasswordResetDoneView')}, name='password_reset'),
    url(r'^done/$', PasswordResetDoneView, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView,
        {'post_reset_redirect': reverse_lazy('PasswordResetCompleteView')}, name='password_reset_confirm'),
    url(r'^complete/$', PasswordResetCompleteView, name='password_reset_complete')
]