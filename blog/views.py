from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import logout


# Create your views here.
def index(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def welcome(request):
    return render(request, 'welcome.html')


@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')


