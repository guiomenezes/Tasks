from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def new_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            
            name_display = first_name if first_name else username
            messages.success(request, f'The user {name_display} was created.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})
