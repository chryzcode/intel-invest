from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('all-packages/', views.allPackages, name='all-packages'),
    path('package/<str:package_id>/', views.pacakageDetail, name='package-detail'),
    path('add-package/', views.addPackage, name='add-package'),
    path('logout/', views.logoutUser, name='logout'),
    path('edit-package/<str:package_id>/', views.editPackage, name='edit-package'),
    path('delete-package/<str:package_id>/', views.deletePackage, name='delete-package'),
    path('faqs-page/', views.faqspage, name='faqs-page'),
    path('about-us/', views.aboutus, name='about-us'),
    path('rules/', views.rules, name='rules'),
]