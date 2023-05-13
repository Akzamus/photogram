from django.urls import path

from .views import profile_view, create_gallery_view, create_picture_view

app_name = 'galleries'

urlpatterns = [
    path('profile/', profile_view, name='my_profile'),
    path('profile/<str:username>/', profile_view, name='profile'),
    path('create-gallery/', create_gallery_view, name='create_gallery'),
    path('create-picture/', create_picture_view, name='create_picture'),
]
