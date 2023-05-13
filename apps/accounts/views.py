from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm


def profile_view(request):
    return render(request, 'accounts/profile.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
