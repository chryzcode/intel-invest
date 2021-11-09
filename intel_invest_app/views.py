from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, PackagesForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.
def loginPage(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
             
    return render(request,'registration/login.html', context)

def registerPage(request):
    form = SignupForm
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect ('home')
        else:
            messages.error(request, 'An error occured during registration')

    return render(request, 'registration/register.html', {'form':form})

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def addPackage(request):
    if request.user.is_superuser:
        form = PackagesForm
        if request.method == 'POST':
            form = PackagesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('all-packages')
        return render(request, 'packages.html', {'form':form})
    else:
        return redirect('home')

@login_required(login_url='login')
def editPackage(request, package_id):
    if request.user.is_superuser:
        package = Packages.objects.get(pk=package_id)
        form = PackagesForm(instance=package)
        if request.method == 'POST':
            form = PackagesForm(request.POST, instance=package)
            if form.is_valid():
                form.save()
                return redirect ('all-packages')
        return render(request, 'packages.html', {'form':form})
    else:
        return redirect('home')

@login_required(login_url='login')
def allPackages(request):
    if request.user.is_superuser:
        packages = Packages.objects.all()
        context = {'packages':packages}
        return render(request, 'all-packages.html', context)
    else:
        return redirect('home')

@login_required(login_url='login')
def deletePackage(request, pk):
    if request.user.is_superuser:
        package = Packages.objects.get(pk=pk)
        package.delete()
        return redirect('all-packages')
    else:
        return redirect('home')

@login_required(login_url='login')
def pacakageDetail(request, package_id):
        package = Packages.objects.get(pk=package_id)
        context = {'package':package}
        return render(request, 'package-detail.html', context)

def faqspage(request):
    return render(request, 'faq-pages.html')

def aboutus(request):
    return render(request, 'about-us.html')

def rules(request):
    return render(request, 'rules.html')

@login_required(login_url='login')
def userProfile(request, username):
    user = get_object_or_404(User, username=username)
    package_invested = Packages.objects.filter(investors=user)
    total_investment_price = 0
    for package in package_invested:
        total_investment_price += package.package_price

    if user == username or user.is_superuser:
        context = {'user':user, 'package_invested':package_invested, 'total_investment_price':total_investment_price}
        return render(request, 'user-profile.html', context)
    else:
        return redirect('user-profile', username= request.user.username)


