from django.urls import path
from apps.accounts.views import register_view, search_users_view, logout_view
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('search/', search_users_view, name='search_users'),
]
