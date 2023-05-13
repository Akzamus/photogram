from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Gallery, Picture

User = get_user_model()


@login_required
def profile_view(request, username=None):
    if not username:
        profile_user = request.user
    else:
        profile_user = get_object_or_404(User, username=username)

    is_own_profile = (request.user == profile_user)

    if 'gallery_id' in request.GET:
        gallery_id = request.GET['gallery_id']
        gallery = get_object_or_404(Gallery, id=gallery_id, user=profile_user)
    else:
        gallery = profile_user.galleries.first()

    pictures = None
    gallery_id = None

    if gallery:
        pictures = Picture.objects.filter(gallery=gallery.id).order_by('-is_favorite', '-created_at')
        gallery_id = gallery.id

    galleries = profile_user.galleries.all()

    context = {
        'is_own_profile': is_own_profile,
        'profile_user': profile_user,
        'gallery_id': gallery_id,
        'galleries': galleries,
        'pictures': pictures,
    }

    return render(request, 'galleries/profile.html', context)
