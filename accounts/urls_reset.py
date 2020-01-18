from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    url(r'^reset-password/$',
    PasswordResetView.as_view(), name='password_reset'),
    url(r'^reset-password/done/$',
    PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset-password/complete/$',
    PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]