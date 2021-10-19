from django.shortcuts import render, redirect
from bhome.models import Home
from django.contrib.auth.models import User
from bhome.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
'''
views are those functions, which are responsible for rendering html from templates
'''


def home(request):
    # function for home page,
    # dictionary is deliver data from python to html templates
    # request.user.is_authenticated is a boolean that tells either user is logged in or not.
    context = {'status': request.user.is_authenticated}
    return render(request, 'index.html', context)


def listings(request):
    # listing contain details of all homes except those which have owners=False
    homes = Home.objects.filter(owners=False)
    context = {'homes': homes, 'status': request.user.is_authenticated}
    return render(request, 'listings.html', context)


def house(request, pk):
    # use pk to receive id as primary key. it get the information of the home with respect to that id
    current_home = Home.objects.get(id=pk)
    context = {'current_home': current_home, 'status': request.user.is_authenticated}
    return render(request, 'house.html', context)


def owners(request):
    # owners houses are returned here in this function and sent to template of owners
    owner_homes = Home.objects.filter(owners=True)
    context = {'homes': owner_homes, 'status': request.user.is_authenticated}
    return render(request, 'owners.html', context)


def services(request):
    # this is for rendering the services template
    context = {'status': request.user.is_authenticated}
    return render(request, 'services.html', context)


def register(request):
    # create a user registration form designed in forms.py and render it on register page
    # if post is sent than form save the user data and redirect user to login page
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form, 'status': request.user.is_authenticated}
    return render(request, 'register.html', context)


def login_page(request):
    # function for login page, login can get you access to the admin panel easily
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    context = {'status': request.user.is_authenticated}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def logout_user(request):
    # logout the current active user
    logout(request)
    return redirect('home')
