from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer

#Registration form 
class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='ConfirmPassword',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model =User
        fields =['username','email','password1','password2']
        labels= {'email':'Email'}
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'})
        }

#Login Form
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

#password change form using PasswordChangeForm

#password reset form

#password reset form-confirm form

#profile model form
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','locality','city','state','zipcode']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'})
        }