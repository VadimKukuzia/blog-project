from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('log-out', views.log_out, name='log-out'),
    path('log-in', views.log_in, name='log-in'),
    path('profile', views.profile, name='profile'),
    path('user/<int:pk>/profile', views.user_profile, name='user-profile'),
]
