from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserData
from .forms import UserForm

def user_list(request):
    users = UserData.objects.all()
    return render(request, 'user_list.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

def profile_user(request, pk):
    user = get_object_or_404(UserData, pk=pk)    
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_user', pk=pk)  # Redirect back to profile page
    else:
        form = UserForm(instance=user)
    return render(request, 'profile_user.html', {'form': form, 'user': user})

def edit_user(request, pk):
    user = get_object_or_404(UserData, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})

def delete_user(request, pk):
    user = get_object_or_404(UserData, pk=pk)
    user.delete()
    return redirect('user_list')