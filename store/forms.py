from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ShippingAddress, Customer, Product, OrderItem


class LoginForm(forms.Form):
   username = forms.CharField(
       label="Username",
       widget=forms.TextInput(
           attrs={
               "class": "form-control"
           }
       ))
   password = forms.CharField(
       label="password",
       widget=forms.PasswordInput(
           attrs={
               "class": "form-control"
           }
       ))


class SignUpForm(UserCreationForm):
   username = forms.CharField(
       label="Username",
       widget=forms.TextInput(
           attrs={
               "class": "form-control"
           }
       ))
   email = forms.EmailField(
       label="Email ",
       widget=forms.EmailInput(
           attrs={
               "class": "form-control"
           }
       ))
   password1 = forms.CharField(
       label="password",
       widget=forms.PasswordInput(
           attrs={
               "class": "form-control"
           }
       ))
   password2 = forms.CharField(
       label="re-enter your password",
       widget=forms.PasswordInput(
           attrs={
               "class": "form-control"
           }
       ))

   class Meta:
       model = User
       fields = ('username', 'email', 'password1', 'password2')


class CustomerSignUpForm(forms.ModelForm):
  name = forms.CharField(
      widget=forms.TextInput(
           attrs={
               "class": "form-control"
           })
    )

  company_name = forms.CharField(
      widget=forms.TextInput(
           attrs={
               "class": "form-control"
           })
    )

  class Meta:
    model = Customer
    fields = ('name', 'company_name')


class ShippingAddressForm(forms.ModelForm):
  class Meta:
    model = ShippingAddress
    exclude =['customer', 'order']


class ProductUpdateForm(forms.ModelForm):
  class Meta:
    model = Product
    exclude = ['', ]


class QuantityForm(forms.Form):
  quantity = forms.IntegerField()