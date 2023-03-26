from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'administrator/base.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username} succesfully.')
        else:
            messages.error(request, f'invalid action ')
        
    form=UserRegistrationForm()
    return render(request, 'user/register.html', {'form':form})
