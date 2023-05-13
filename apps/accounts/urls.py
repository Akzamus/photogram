from django.urls import path
from apps.accounts.views import profile_view, register_view
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login')
]
