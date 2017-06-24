from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserForm
# Create your views here.

def login(request):

    form = UserForm()
    return render(request, 'users/login.html', {'form': form})
