from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('log-out', views.log_out, name='log-out'),
    path('log-in', views.log_in, name='log-in'),
    path('profile', views.profile, name='profile'),
    path('user/<str:username>/profile', views.user_profile, name='user-profile'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),
         name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name='password_reset_complete'),
]
