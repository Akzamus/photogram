from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import GalleryForm, PictureForm
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
        gallery = get_object_or_404(Gallery, id=gallery_id)
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
        'selected_gallery_id': gallery_id,
        'galleries': galleries,
        'pictures': pictures,
    }

    return render(request, 'galleries/profile.html', context)


@login_required
def create_gallery_view(request):
    if request.method == 'POST':
        form = GalleryForm(request.user, data=request.POST)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.user = request.user
            gallery.save()
            return redirect('galleries:my_profile')
    else:
        form = GalleryForm(user=request.user)
    return render(request, 'galleries/create_gallery.html', {'form': form})


@login_required
def create_picture_view(request):
    if request.method == 'POST':
        form = PictureForm(request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = request.user
            picture.save()
            return redirect('galleries:my_profile')
    else:
        form = PictureForm(user=request.user)
    return render(request, 'galleries/create_picture.html', {'form': form})
