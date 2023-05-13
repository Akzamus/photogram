from django.urls import path

from .views import profile_view

app_name = 'galleries'

urlpatterns = [
    path('profile/', profile_view, name='my_profile'),
    path('profile/<str:username>/', profile_view, name='profile'),
]
