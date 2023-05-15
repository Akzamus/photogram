from django.urls import path
from apps.accounts.views import register, search_users, logout_user
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', logout_user, name='logout'),
    path('search/', search_users, name='search_users'),
]
