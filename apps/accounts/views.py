from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import logout

User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def search_users(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        users = User.objects.filter(username__icontains=query, is_staff=False)
        return render(request, 'accounts/search_users.html', {'users': users})


def logout_user(request):
    logout(request)
    return redirect('accounts:login')
