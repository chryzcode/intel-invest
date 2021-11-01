from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, PackagesForm

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

def addPackage(request):
    form = PackagesForm
    if request.method == 'POST':
        form = PackagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    return render(request, 'packages.html', {'form':form})

def editPackage(request, pk):
    pacakage = Packages.objects.get(pk = pk)
    form =  PackagesForm(instance=package)
    if request.method == 'POST':
        form = PackagesForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('view-note', pk=note.pk)
    context = {'form':form}
    return render(request, 'packages.html', context)

def allPackages(request):
    packages = Packages.objects.all()
    context = {'packages':packages}
    return render(request, 'all-packages.html', context)

def deletePackage(request, pk):
    package = Packages.objects.get(pk=pk)
    package.delete()
    return redirect('all-packages')

def pacakageDetail(request, pk):
    package = Packages.objects.get(pk=pk)
    context = {'package':package}
    return render(request, 'package-detail.html', context)

def allAdminPage(request):
    return render(request, 'admin-page.html')
