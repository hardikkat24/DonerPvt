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
       label="Password ",
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
       label="Email",
       widget=forms.EmailInput(
           attrs={
               "class": "form-control"
           }
       ))
   password1 = forms.CharField(
       label="Password",
       widget=forms.PasswordInput(
           attrs={
               "class": "form-control"
           }
       ))
   password2 = forms.CharField(
       label="Re-enter your Password",
       widget=forms.PasswordInput(
           attrs={
               "class": "form-control"
           }
       ))

   class Meta:
       model = User
       fields = ('username', 'email', 'password1', 'password2')


class CustomerSignUpForm (forms.ModelForm):
  fname = forms.CharField(
      label="First Name",
      widget=forms.TextInput(
           attrs={
               "class": "form-control"
           })
    )

  lname = forms.CharField(
      label="Last Name",
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
    fields = ('fname', 'lname', 'company_name')


class ShippingAddressForm(forms.ModelForm):
  country = forms.CharField(
      label="Country",
      widget=forms.TextInput(
           attrs={
               "class": "form-control"
           })
    )

  state = forms.CharField(
      label="State",
      widget=forms.TextInput(
           attrs={
               "class": "form-control"
           })
    )

  class Meta:
    model = ShippingAddress
    exclude =['customer', 'order']


class ProductUpdateForm(forms.ModelForm):
  class Meta:
    model = Product
    exclude = ['', ]


class QuantityForm(forms.Form):
  quantity = forms.IntegerField()