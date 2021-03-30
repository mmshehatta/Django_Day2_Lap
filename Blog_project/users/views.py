from django.shortcuts import render , redirect
from django.contrib.auth .forms import UserCreationForm

# Create your views here.

# ******************* register function *******
def register(request):
    form = UserCreationForm()
    context={
        'RegisterForm':form
    }
    return render(request , 'users/register.html' , context)