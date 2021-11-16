from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    full_name = forms.CharField(max_length = 200)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('full_name', 'username', 'email','password1', 'password2')

    def __init__ (self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)


        self.fields['full_name'].widget.attrs['class']= 'form-control'
        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['email'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'


class PackagesForm(forms.ModelForm):
    class Meta:
        model = Packages
        fields = ('package_name', 'package_price', 'package_description')

        widgets={
                'package_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Package Name'}),
                'package_price':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'$ Package Price'}),
                'package_description':forms.Textarea(attrs={'class':'form-control',  'placeholder':'Package description...'}),
        }

class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'full_name', 
            'email', 
            'username',
        ]

        widgets={
                'full_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}),
                'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
                'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
        }

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        exclude = ['user']

        widgets={
            'transanction_hash':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Payment transanction hash'}),
            'cryptocurrency':forms.Select(choices= Cryptocurrency.objects.all().values_list('name', 'name'), attrs={'class':'form-control'}),
            'package':forms.Select(choices= Packages.objects.all().values_list('package_name', 'package_name'), attrs={'class':'form-control'}),
    }

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

class UserWalletForm(ModelForm):
    class Meta:
        model = UserWallet
        fields = "__all__"
        exclude = ['user']

        widgets={
            'bitcoin':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bitcoin wallet'}),
            'ethereum':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ethereum wallet'}),
            'litecoin':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Litecoin wallet'}),
            'bnb':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bnb wallet'}),
            'busd':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Busd wallet'}),
            'usdt':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Usdt wallet'}),
    }

    def user (self, user):
        self.user = user.id

    def __init__(self, *args, **kwargs):
        super(UserWalletForm, self).__init__(*args, **kwargs)


class ConfirmPaymentForm(ModelForm):
    class Meta:
        model = ConfirmPayment
        fields = "__all__"
        exlude = ['user']

        widgets={
            'reciever_email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Reciever Email'}),
            'reciever_account':forms.Select(choices= User.objects.all().values_list('email', 'email'), attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Put in a message'}),
    }

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)