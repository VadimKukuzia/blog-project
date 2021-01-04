from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('log-out', views.log_out, name='log-out'),
    path('log-in', views.log_in, name='log-in'),
    path('profile', views.profile, name='profile'),
    path('user/<str:username>/profile', views.user_profile, name='user-profile'),
    path('reset-password', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),
         name='reset-password'),
]
