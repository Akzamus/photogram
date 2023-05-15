from django.urls import path

from .views import profile, create_gallery, create_picture, picture_detail

app_name = 'galleries'

urlpatterns = [
    path('profile/', profile, name='my_profile'),
    path('profile/<str:username>/', profile, name='profile'),
    path('create-gallery/', create_gallery, name='create_gallery'),
    path('create-picture/', create_picture, name='create_picture'),
    path('pictures/<int:id>/', picture_detail, name='picture'),
]
