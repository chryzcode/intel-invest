from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from datetime import date, timedelta


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
        user = request.user
        package = Packages.objects.get(pk=package_id)
        context = {'package':package, 'user':user}
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
    wallets = user.userwallet_set.filter(user=user)[:1]
    total_investment_price = 0
    for package in package_invested:
        total_investment_price += package.package_price

    if request.user == user.is_superuser or request.user :
        context = {'user':user, 'package_invested':package_invested, 'total_investment_price':total_investment_price, 'wallets':wallets}
        return render(request, 'user-profile.html', context)
    else:
        return redirect('home')


@login_required(login_url='login')
def payment(request):
    sender_email = request.user.email
    form = PaymentForm
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'Investment Payment {form.cleaned_data["email"]}'
            email_message = {
            'email_cryptocurrency':form.cleaned_data["cryptocurrency"],
            'transanction_hash':form.cleaned_data["transanction_hash"],
            'package':form.cleaned_data["package"],
            'screenshot':form.cleaned_data["screenshot"],
            }
            send_mail(email_subject, email_message, sender_email, settings.COMPANY_EMAIL)
    context = {'form':form}
    return render(request, 'payment.html', context)

@login_required(login_url='login')
def addUserWallet(request):
    form = UserWalletForm
    wallets = UserWallet.objects.filter(user=request.user)
    if wallets:
        return redirect('user-profile', request.user.username)
    
    if request.method == 'POST':
        form = UserWalletForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user                                                
            form.save()
            return redirect ('user-profile', request.user.username)

    return render(request, 'add-user-wallets.html', {'form':form})

def editUserWallet(request):
    wallets = UserWallet.objects.filter(user=request.user).first()
    form = UserWalletForm(instance=wallets)
    if request.method == 'POST':
        form = UserWalletForm(request.POST, instance=wallets)
        if form.is_valid():
            form.save()
            return redirect ('user-profile', request.user.username)
    return render(request, 'add-user-wallets.html', {'form':form})

def confirmedPayment(request):
    sender_email = request.user.email
    form = ConfirmPaymentForm
    if request.method == 'POST':
        form = ConfirmPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'Confirmed Investment Payment {form.cleaned_data["email"]}'
            email_message = {
            'reciever_email':form.cleaned_data["reciever_email"],
            'reciever_account':form.cleaned_data["reciever_account"],
            'pacakage':form.cleaned_data["pacakage"],
            'body':form.cleaned_data["body"],
            'screenshot':form.cleaned_data["screenshot"],
            }
            send_mail(email_subject, email_message, sender_email, settings.COMPANY_EMAIL)
            reciever_account = form.cleaned_data["reciever_account"]
            an_investor = User.objects.get(user=reciever_account)
            package = Packages.objects.get(pk=form.cleaned_data["pacakage"])
            pacakage.investors.add(an_investor)
            return redirect('home')  
    context = {'form':form}
    return render(request, 'confirm-payment.html', context)


