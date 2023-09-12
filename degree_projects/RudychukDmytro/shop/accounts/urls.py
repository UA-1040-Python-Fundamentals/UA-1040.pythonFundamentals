from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('', views.signup, name='accounts'),
    path('login/', views.login_view, name='login'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='password_change.html',
    ), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'),
         name='password_change_done'
    ),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('oauth/', include("social_django.urls", namespace="social")),
]