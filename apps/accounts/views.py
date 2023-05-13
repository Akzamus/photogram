from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import logout

User = get_user_model()


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def search_users_view(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        results = User.objects.filter(username__icontains=query)
        return render(request, 'accounts/search_users.html', {'results': results})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')
